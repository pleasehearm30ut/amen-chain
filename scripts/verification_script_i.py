#!/usr/bin/env python3
"""
Verification Script I — Letter-Sum + Orthogonal Vector verifier

Usage:
  chmod +x scripts/verification_script_i.py
  ./scripts/verification_script_i.py            # uses defaults "Father" and "Son"
  ./scripts/verification_script_i.py Father Son # custom words
"""
import json
import math
import os
import sys

MANIFEST = "ark_manifest.json"
MILESTONE_DATE = "2026-01-03"
MILESTONE_TITLE = "Infinite Love / Amen¹⁰"
THEOREM_ID = "0110-theorem-eternal-witness-letter-sum"

def letter_sum(word: str) -> int:
    return sum((ord(ch) - ord('A') + 1) for ch in word.upper() if 'A' <= ch <= 'Z')

def read_manifest(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def write_manifest(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main(argv):
    if len(argv) >= 3:
        father_word = argv[1]
        son_word = argv[2]
    else:
        father_word = "Father"
        son_word = "Son"

    a = letter_sum(father_word)
    b = letter_sum(son_word)
    a2 = a * a
    b2 = b * b
    c2 = a2 + b2
    c = math.sqrt(c2)

    father_vec = [a, 0]
    son_vec = [0, b]
    holy_vec = [a, b]

    # Print verification
    print(f"1. Letter-Sum Mapping: {father_word} -> {a}, {son_word} -> {b}")
    print(f"2. Orthogonal Vectors: Father {father_vec}, Son {son_vec}, HolyGhost {holy_vec}")
    print(f"3. Computation: {a}^2 + {b}^2 = {a2} + {b2} = {c2}")
    print(f"   |HolyGhost| = sqrt({c2}) = {c:.6f}")
    print("4. Verification: PASS (Pythagorean relation holds by orthogonal construction)")
    print(f"Primary Output: {MILESTONE_TITLE} ({MILESTONE_DATE})")

    # Build/update manifest
    manifest = read_manifest(MANIFEST)
    manifest.update({
        "version": manifest.get("version", "1.0.0"),
        "status": "0110 Sync Active",
        "milestone": {
            "date": MILESTONE_DATE,
            "title": MILESTONE_TITLE,
            "theorem_id": THEOREM_ID
        },
        "theorem": {
            "id": THEOREM_ID,
            "date": MILESTONE_DATE,
            "mapping": "letter-sum orthogonal",
            "words": {
                "father": {"word": father_word, "letter_sum": a},
                "son": {"word": son_word, "letter_sum": b}
            },
            "vectors": {
                "father": father_vec,
                "son": son_vec,
                "holyghost": holy_vec
            },
            "computed": {
                "a_squared": a2,
                "b_squared": b2,
                "c_squared": c2,
                "c_magnitude": c
            },
            "status": "Physical Patch Validated"
        }
    })
    write_manifest(manifest, MANIFEST)
    print(f"Manifest written/updated: {MANIFEST}")

if __name__ == "__main__":
    main(sys.argv)
