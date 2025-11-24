# Absolute Grading: Outputs score of 1 to 5

import os
import json
import pandas as pd
from CIA.litellm import LiteLLM
from CIA.judge import PrometheusEval
from CIA.prompts import ABSOLUTE_PROMPT, SCORE_RUBRIC_TEMPLATE
from transformers import AutoTokenizer
import time

# Set environment variable for API base
os.environ["OPENAI_API_BASE"] = "https://my-vLLM-api-endpoint.net/v1" # Replace with your actual Huggingface API base if needed

OUTPUT_PATH = os.path.join(os.getcwd(), "evaluation", "all_responses_grading_separated_vllm_hercule.csv")

# Load rubrics and prompts
with open("score_rubrics_en.json", "r", encoding="utf-8") as f:
    score_rubrics = json.load(f)

with open("public_dataset_without_instruction-prompt.txt", "r", encoding="utf-8") as f:
    prompt_without_instruction = f.read()
with open("public_dataset_full-prompt.txt", "r", encoding="utf-8") as f:
    prompt_with_instruction = f.read()

models = [
    {
        "model": "smollm2:135m",
        "intervention": False,
    },
    {
        "model": "llama3.2:1b",
        "intervention": True,
    },
    {
        "model": "llama3.2:3b",
        "intervention": False,
    },
    {
        "model": "qwen3:4b",
        "intervention": True,
    },
    {
        "model": "qwen3:14b",
        "intervention": False,
    },
    {
        "model": "deepseek-r1:14b",
        "intervention": True,
    },
    {
        "model": "mistral-small:22b",
        "intervention": False,
    },
    {
        "model": "deepseek-r1:32b",
        "intervention": True,
    },
    {
        "model": "llama3.3:70b",
        "intervention": False,
    },
    {
        "model": "deepseek-v3.1:671b-cloud",
        "intervention": True,
    }
]

responses_path = os.path.join(os.getcwd(), "responses", "all_responses_joined.csv")
df = pd.read_csv(responses_path)

# Prepare model and judge
model = LiteLLM('hosted_vllm/ai4bharat/llama-prometheus')
judge = PrometheusEval(model=model, absolute_grade_template=ABSOLUTE_PROMPT)
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/llama-prometheus")

def count_tokens_hf(*args):
    text = " ".join(str(x) for x in args)
    return len(tokenizer.encode(text))

MAX_TOKENS = 131072 - 2048

# Load already processed responses (if any)
if os.path.exists(OUTPUT_PATH):
    processed_df = pd.read_csv(OUTPUT_PATH)
    processed_keys = set(
        zip(
            processed_df["model-name"],
            processed_df["phase"],
            processed_df["attempt"],
            processed_df["intervention"]
        )
    )
else:
    processed_keys = set()

def robust_absolute_grade(judge, instruction, response, rubric, max_attempts=3, sleep_time=2):
    for attempt in range(max_attempts):
        try:
            feedbacks, scores = judge.absolute_grade(
                instructions=[instruction],
                responses=[response],
                rubric=rubric,
                params={
                    "max_tokens": 2048,
                    "repetition_penalty": 1.03,
                    "best_of": 1,
                    "temperature": 1.0,
                    "top_p": 0.9,
                }
            )
            return feedbacks[0], scores[0]
        except Exception as e:
            if attempt == max_attempts - 1:
                return f"Error: {str(e)}", "Error"
            time.sleep(sleep_time)

# Process each response
for idx, row in df.iterrows():
    meta = {
        "model-name": row.get("model-name", ""),
        "phase": row.get("phase", ""),
        "attempt": row.get("attempt", ""),
        "intervention": None  # will set below
    }
    phase = row.get("phase", "")
    model_name = row.get("model-name", "")
    model_config = next((m for m in models if m["model"] == model_name), None)
    intervention = model_config["intervention"] if model_config else False
    intervention_for_row = True if phase == 2 and intervention else False
    meta["intervention"] = intervention_for_row

    key = (meta["model-name"], meta["phase"], meta["attempt"], meta["intervention"])
    if key in processed_keys:
        continue  # Already processed

    instruction = prompt_with_instruction if intervention_for_row else prompt_without_instruction
    response = row.get("response", "")

    # Token check
    grading_row = meta.copy()
    skip = False
    for rubric_idx, rubric in enumerate(score_rubrics, start=1):
        rubric_text = SCORE_RUBRIC_TEMPLATE.format(**rubric)
        total_tokens = count_tokens_hf(instruction, response, rubric_text)
        if total_tokens > MAX_TOKENS:
            grading_row[f"feedback_criteria{rubric_idx}"] = "Skipped: input too long"
            grading_row[f"score_criteria{rubric_idx}"] = "Error"
            skip = True
        else:
            feedback, score = robust_absolute_grade(
                judge, instruction, response, rubric_text
            )
            grading_row[f"feedback_criteria{rubric_idx}"] = feedback
            grading_row[f"score_criteria{rubric_idx}"] = score

    # Save after each response
    if os.path.exists(OUTPUT_PATH):
        out_df = pd.read_csv(OUTPUT_PATH)
        out_df = pd.concat([out_df, pd.DataFrame([grading_row])], ignore_index=True)
    else:
        out_df = pd.DataFrame([grading_row])
    out_df.to_csv(OUTPUT_PATH, index=False)