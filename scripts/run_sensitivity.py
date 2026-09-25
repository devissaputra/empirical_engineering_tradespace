#!/usr/bin/env python3
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.model import load_all_objectives, sensitivity_analysis

def build_payload():
    return {
        "study": "Empirical Engineering Design Trade Space: Concrete Slump Experiments",
        "purpose": "Test whether the observed decision set depends on treating slump as an optimization objective.",
        "interpretation_note": (
            "The 10 cm and 20 cm slump cutoffs are analytical sensitivity thresholds, "
            "not universal engineering requirements."
        ),
        "specifications": sensitivity_analysis(load_all_objectives()),
    }

def build_csv_rows(payload):
    rows = []
    for s in payload["specifications"]:
        rows.append({
            "specification": s["specification"],
            "eligible_n": s["eligible_n"],
            "pareto_count": s["pareto_count"],
            "baseline_overlap_count": s["baseline_overlap_count"],
            "baseline_retention": s["baseline_retention"],
            "jaccard_with_baseline": s["jaccard_with_baseline"],
            "frontier_ids": " ".join(str(x) for x in s["frontier_ids"]),
        })
    return rows

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    payload = build_payload()
    expected_json = ROOT / "results/sensitivity_summary.json"
    expected_csv = ROOT / "data/derived/sensitivity_results.csv"
    if args.check:
        packaged = json.loads(expected_json.read_text(encoding="utf-8"))
        if packaged != payload:
            raise SystemExit("FAIL: packaged sensitivity JSON differs from recomputation")
        with expected_csv.open(newline="", encoding="utf-8") as f:
            packaged_csv = list(csv.DictReader(f))
        computed_csv = build_csv_rows(payload)
        for row in computed_csv:
            row.update({
                "eligible_n": str(row["eligible_n"]),
                "pareto_count": str(row["pareto_count"]),
                "baseline_overlap_count": str(row["baseline_overlap_count"]),
                "baseline_retention": str(row["baseline_retention"]),
                "jaccard_with_baseline": str(row["jaccard_with_baseline"]),
            })
        if packaged_csv != computed_csv:
            raise SystemExit("FAIL: packaged sensitivity CSV differs from recomputation")
        print("sensitivity_check: PASS")
        return
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
