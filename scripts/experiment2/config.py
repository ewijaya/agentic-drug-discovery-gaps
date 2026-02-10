"""Configuration for Experiment 2: LLM knowledge probing across drug modalities."""

from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
QUESTIONS_PATH = BASE_DIR / "questions.json"
RESPONSES_DIR = BASE_DIR / "responses"
SCORES_DIR = BASE_DIR / "scores"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_FIGURES_DIR = RESULTS_DIR / "figures"

MODELS = [
    {
        "name": "Kimi K2.5",
        "tag": "kimi-k2.5:cloud",
        "response_file": "kimi-k2.5.jsonl",
    },
    {
        "name": "DeepSeek V3.2",
        "tag": "deepseek-v3.2:cloud",
        "response_file": "deepseek-v3.2.jsonl",
    },
    {
        "name": "Qwen 3 Next 80B",
        "tag": "qwen3-next:80b-cloud",
        "response_file": "qwen3-next-80b.jsonl",
    },
    {
        "name": "Gemini 3 Flash",
        "tag": "gemini-3-flash-preview:cloud",
        "response_file": "gemini-3-flash.jsonl",
    },
]

SYSTEM_PROMPT = (
    "You are a pharmaceutical scientist with expertise in drug discovery. "
    "Answer the following question accurately and concisely. "
    "Include specific numbers, ranges, or examples where relevant. "
    "If you are uncertain, say so rather than guessing."
)

API_DELAY_SECONDS = 3
MAX_RETRIES = 3
RETRY_BASE_SECONDS = 10
TEMPERATURE = 0.3
MAX_TOKENS = 1024
RANDOM_SEED = 42

CLAUDE_CLI = "/home/ubuntu/.local/bin/claude"
CLAUDE_MODEL = "sonnet"
CLAUDE_DELAY_SECONDS = 1
EXPERT_SUBSET_FRACTION = 0.2

EXPECTED_QUESTION_COUNT = 100
EXPECTED_PAIR_COUNT = 50
EXPECTED_CATEGORY_COUNT_PER_DOMAIN = 10
EXPECTED_CATEGORIES = [
    "SAR Reasoning",
    "ADMET / Pharmacokinetic Properties",
    "Generative Design Strategies",
    "Optimization Approaches",
    "Assay Interpretation",
]
EXPECTED_DOMAINS = ["small_molecule", "peptide"]
REQUIRED_QUESTION_FIELDS = [
    "id",
    "category",
    "domain",
    "pair_id",
    "question",
    "reference_answer",
    "key_concepts",
    "difficulty",
]

OKABE_ITO_SKY_BLUE = "#56B4E9"
OKABE_ITO_VERMILLION = "#D55E00"
OFF_WHITE = "#FAFAFA"
CHARCOAL = "#333333"


def ensure_directories() -> None:
    """Ensure output directories exist."""
    RESPONSES_DIR.mkdir(parents=True, exist_ok=True)
    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    RESULTS_FIGURES_DIR.mkdir(parents=True, exist_ok=True)
