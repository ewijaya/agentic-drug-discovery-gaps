"""Pre-flight validation for Experiment 2 question set."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from config import (
    EXPECTED_CATEGORIES,
    EXPECTED_CATEGORY_COUNT_PER_DOMAIN,
    EXPECTED_DOMAINS,
    EXPECTED_PAIR_COUNT,
    EXPECTED_QUESTION_COUNT,
    QUESTIONS_PATH,
    REQUIRED_QUESTION_FIELDS,
)

PROMPT_VERB_PATTERN = re.compile(
    r"\b("
    r"explain|describe|compare|discuss|provide|outline|analyze|evaluate|justify|predict|"
    r"calculate|compute|identify|summarize|give|list|state|define|name|estimate|propose|interpret"
    r")\b",
    re.IGNORECASE,
)


def load_questions(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("questions.json must contain a top-level JSON array.")
    return data


def is_non_empty(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return len(value) > 0
    return True


def looks_like_prompt(text: str) -> bool:
    stripped = text.strip()
    return stripped.endswith("?") or bool(PROMPT_VERB_PATTERN.search(stripped))


def validate_questions(questions: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []

    if len(questions) != EXPECTED_QUESTION_COUNT:
        errors.append(
            f"Expected exactly {EXPECTED_QUESTION_COUNT} questions, found {len(questions)}."
        )

    question_ids: list[str] = []
    pair_to_domains: dict[str, set[str]] = defaultdict(set)
    pair_counts: Counter[str] = Counter()
    category_domain_counts: Counter[tuple[str, str]] = Counter()

    for i, q in enumerate(questions, start=1):
        if not isinstance(q, dict):
            errors.append(f"Row {i}: each question must be an object.")
            continue

        for field in REQUIRED_QUESTION_FIELDS:
            if field not in q:
                errors.append(f"Row {i}: missing required field '{field}'.")
            elif not is_non_empty(q[field]):
                errors.append(f"Row {i}: field '{field}' must be non-empty.")

        qid = q.get("id")
        pair_id = q.get("pair_id")
        category = q.get("category")
        domain = q.get("domain")
        prompt = q.get("question", "")

        if isinstance(qid, str):
            question_ids.append(qid)
        if isinstance(pair_id, str):
            pair_counts[pair_id] += 1
        if isinstance(pair_id, str) and isinstance(domain, str):
            pair_to_domains[pair_id].add(domain)
        if isinstance(category, str) and isinstance(domain, str):
            category_domain_counts[(category, domain)] += 1

        if isinstance(domain, str) and domain not in EXPECTED_DOMAINS:
            errors.append(
                f"Row {i} ({qid or 'unknown id'}): invalid domain '{domain}'. "
                f"Expected one of {EXPECTED_DOMAINS}."
            )

        if isinstance(category, str) and category not in EXPECTED_CATEGORIES:
            errors.append(
                f"Row {i} ({qid or 'unknown id'}): invalid category '{category}'."
            )

        if not isinstance(q.get("key_concepts"), list) or not q.get("key_concepts"):
            errors.append(
                f"Row {i} ({qid or 'unknown id'}): key_concepts must be a non-empty list."
            )

        if not isinstance(prompt, str) or not looks_like_prompt(prompt):
            errors.append(
                f"Row {i} ({qid or 'unknown id'}): question must end with '?' or be an explicit prompt."
            )

    id_counts = Counter(question_ids)
    duplicates = sorted([qid for qid, c in id_counts.items() if c > 1])
    if duplicates:
        errors.append(f"Duplicate question ids found: {', '.join(duplicates)}")

    if len(pair_counts) != EXPECTED_PAIR_COUNT:
        errors.append(
            f"Expected exactly {EXPECTED_PAIR_COUNT} unique pair_ids, found {len(pair_counts)}."
        )

    for pair_id, count in sorted(pair_counts.items()):
        if count != 2:
            errors.append(f"pair_id '{pair_id}' has {count} questions; expected 2.")
            continue
        domains = pair_to_domains[pair_id]
        if domains != set(EXPECTED_DOMAINS):
            errors.append(
                f"pair_id '{pair_id}' must include exactly one small_molecule and one peptide question."
            )

    for category in EXPECTED_CATEGORIES:
        for domain in EXPECTED_DOMAINS:
            observed = category_domain_counts[(category, domain)]
            if observed != EXPECTED_CATEGORY_COUNT_PER_DOMAIN:
                errors.append(
                    f"Category/domain count mismatch for '{category}' + '{domain}': "
                    f"expected {EXPECTED_CATEGORY_COUNT_PER_DOMAIN}, found {observed}."
                )

    return errors


def main() -> int:
    if not QUESTIONS_PATH.exists():
        print(f"ERROR: questions file not found at {QUESTIONS_PATH}")
        return 1

    try:
        questions = load_questions(QUESTIONS_PATH)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR: failed to load questions: {exc}")
        return 1

    errors = validate_questions(questions)
    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("VALIDATION PASSED")
    print(f"- questions: {len(questions)}")
    print(f"- unique pair_ids: {len({q['pair_id'] for q in questions})}")
    print(f"- categories: {len(EXPECTED_CATEGORIES)}")
    print(f"- domains: {', '.join(EXPECTED_DOMAINS)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
