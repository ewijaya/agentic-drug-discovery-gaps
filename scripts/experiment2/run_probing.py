"""Run Experiment 2 probing across all configured Ollama Cloud models."""

from __future__ import annotations

import json
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ollama import Client

from config import (
    API_DELAY_SECONDS,
    MAX_RETRIES,
    MAX_TOKENS,
    MODELS,
    QUESTIONS_PATH,
    RANDOM_SEED,
    RESPONSES_DIR,
    RETRY_BASE_SECONDS,
    SYSTEM_PROMPT,
    TEMPERATURE,
    ensure_directories,
)


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def load_questions() -> list[dict[str, Any]]:
    with QUESTIONS_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("questions.json must be a list")
    return data


def response_path_for_model(model_cfg: dict[str, str]) -> Path:
    return RESPONSES_DIR / model_cfg["response_file"]


def load_answered_question_ids(path: Path) -> set[str]:
    answered: set[str] = set()
    if not path.exists():
        return answered

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            qid = row.get("question_id")
            success = row.get("success") is True
            if isinstance(qid, str) and success:
                answered.add(qid)
    return answered


def extract_response_text(response: Any) -> str:
    if hasattr(response, "message") and getattr(response.message, "content", None) is not None:
        return str(response.message.content)
    if isinstance(response, dict):
        message = response.get("message")
        if isinstance(message, dict):
            content = message.get("content")
            if content is not None:
                return str(content)
    raise ValueError(f"Unable to extract response content from object of type {type(response)}")


def is_retryable_error(exc: Exception) -> bool:
    if isinstance(exc, ConnectionError):
        return True
    status_code = getattr(exc, "status_code", None)
    if status_code in {429, 503}:
        return True
    text = str(exc)
    return "429" in text or "503" in text


def call_model_with_retry(
    client: Client,
    model_tag: str,
    question_text: str,
) -> tuple[str | None, int, str | None]:
    """Return (response_text, latency_ms, error_message)."""
    attempt = 0
    while True:
        attempt += 1
        start = time.perf_counter()
        try:
            response = client.chat(
                model=model_tag,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question_text},
                ],
                options={
                    "temperature": TEMPERATURE,
                    "num_predict": MAX_TOKENS,
                    "think": False,
                },
            )
            latency_ms = int((time.perf_counter() - start) * 1000)
            response_text = extract_response_text(response)
            if response_text.strip():
                return response_text, latency_ms, None

            if attempt > MAX_RETRIES:
                return None, latency_ms, "ValueError: Empty response content from model"

            backoff = RETRY_BASE_SECONDS * (2 ** (attempt - 1))
            print(
                f"  retryable error on attempt {attempt}/{MAX_RETRIES} for {model_tag}: "
                "empty response content; "
                f"sleeping {backoff}s"
            )
            time.sleep(backoff)
            continue
        except Exception as exc:  # noqa: BLE001
            latency_ms = int((time.perf_counter() - start) * 1000)
            if attempt > MAX_RETRIES or not is_retryable_error(exc):
                return None, latency_ms, f"{type(exc).__name__}: {exc}"
            backoff = RETRY_BASE_SECONDS * (2 ** (attempt - 1))
            print(
                f"  retryable error on attempt {attempt}/{MAX_RETRIES} for {model_tag}: {exc}; "
                f"sleeping {backoff}s"
            )
            time.sleep(backoff)


def append_jsonl(path: Path, row: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def model_run(
    client: Client,
    model_cfg: dict[str, str],
    questions: list[dict[str, Any]],
    model_index: int,
) -> tuple[int, int, int]:
    model_name = model_cfg["name"]
    model_tag = model_cfg["tag"]
    out_path = response_path_for_model(model_cfg)
    answered = load_answered_question_ids(out_path)

    rng = random.Random(RANDOM_SEED + model_index)
    shuffled = list(questions)
    rng.shuffle(shuffled)

    total = 0
    successes = 0
    failures = 0

    print(f"\n=== Model: {model_name} ({model_tag}) ===")
    print(f"Response file: {out_path}")
    print(f"Already answered (resumption): {len(answered)}")

    for q in shuffled:
        qid = q["id"]
        if qid in answered:
            continue

        total += 1
        print(f"[{model_name}] {qid} ({total} new)")

        response_text, latency_ms, error = call_model_with_retry(
            client=client,
            model_tag=model_tag,
            question_text=q["question"],
        )

        response_id = f"{model_tag}|{qid}"
        row = {
            "response_id": response_id,
            "question_id": qid,
            "pair_id": q["pair_id"],
            "category": q["category"],
            "domain": q["domain"],
            "question_text": q["question"],
            "model": model_name,
            "model_tag": model_tag,
            "response_text": response_text or "",
            "latency_ms": latency_ms,
            "timestamp": utc_now_iso(),
            "success": error is None,
            "error": error,
        }

        append_jsonl(out_path, row)

        if error is None:
            successes += 1
            answered.add(qid)
        else:
            failures += 1
            print(f"  ERROR for {qid}: {error}")

        time.sleep(API_DELAY_SECONDS)

    print(
        f"Completed {model_name}: new_calls={total}, successes={successes}, failures={failures}, "
        f"existing={len(load_answered_question_ids(out_path)) - successes}"
    )
    return total, successes, failures


def build_client() -> Client:
    api_key = os.environ.get("OLLAMA_API_KEY")
    if not api_key:
        raise RuntimeError("OLLAMA_API_KEY environment variable is required.")

    return Client(
        host="https://ollama.com",
        headers={"Authorization": f"Bearer {api_key}"},
    )


def main() -> int:
    ensure_directories()
    questions = load_questions()
    client = build_client()

    start = time.perf_counter()
    total_calls = 0
    total_successes = 0
    total_failures = 0

    for idx, model_cfg in enumerate(MODELS):
        calls, successes, failures = model_run(client, model_cfg, questions, idx)
        total_calls += calls
        total_successes += successes
        total_failures += failures

    elapsed = time.perf_counter() - start
    print("\n=== Probing Summary ===")
    print(f"Total new API calls: {total_calls}")
    print(f"Successes: {total_successes}")
    print(f"Failures: {total_failures}")
    print(f"Total wall time: {elapsed:.2f} sec")
    return 0 if total_failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
