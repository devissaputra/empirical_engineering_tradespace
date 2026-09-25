#!/usr/bin/env python3
import argparse
import csv
import io
import json
import statistics
import urllib.request
from pathlib import Path

from research.model import pareto_front

ROOT = Path(__file__).resolve().parents[1]
URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/slump/slump_test.data"

def fetch_rows():
    text = urllib.request.urlopen(URL, timeout=30).read().decode("utf-8-sig")
    raw = list(csv.DictReader(io.StringIO(text)))
    return [
        {
            "experiment_id": int(float(r["No"])),
            "cement": float(r["Cement"]),
            "slump_cm": float(r["SLUMP(cm)"]),
            "strength_mpa": float(r["Compressive Strength (28-day)(Mpa)"]),
        }
        for r in raw
    ]

def summarize(rows):
    front = pareto_front(rows)
    summary = {
        "study": "Empirical Engineering Design Trade Space: Concrete Slump Experiments",
        "headline_metrics": {
            "n_experiments": len(rows),
            "cement_mean": round(statistics.mean(r["cement"] for r in rows), 2),
            "strength_mean_mpa": round(statistics.mean(r["strength_mpa"] for r in rows), 2),
            "slump_mean_cm": round(statistics.mean(r["slump_cm"] for r in rows), 2),
            "pareto_count": len(front),
            "pareto_fraction": round(len(front) / len(rows), 3),
            "max_strength_mpa": max(r["strength_mpa"] for r in rows),
            "min_cement_kg_m3": min(r["cement"] for r in rows),
        },
        "finding": (
            "Twenty-three of 103 observed experiments are non-dominated under the stated "
            "three-objective rule. The frontier includes both very high-strength mixes and "
            "much lower-cement mixes, so a single-score ranking would erase genuine trade-offs."
        ),
        "source": "UCI Concrete Slump Test",
        "retrieved": "2026-09-25",
    }
    return summary, front

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = fetch_rows()
    summary, front = summarize(rows)
    payload = {
        "summary": summary,
        "frontier_experiment_ids": [r["experiment_id"] for r in front],
    }
    if args.check:
        packaged = json.loads((ROOT / "results/empirical_summary.json").read_text(encoding="utf-8"))
        if packaged["headline_metrics"] != summary["headline_metrics"]:
            raise SystemExit("FAIL: public-source rebuild differs from packaged headline metrics")
        expected_ids = {
            int(r["experiment_id"])
            for r in csv.DictReader(
                (ROOT / "data/derived/primary_results.csv").open(encoding="utf-8")
            )
        }
        if expected_ids != set(payload["frontier_experiment_ids"]):
            raise SystemExit("FAIL: public-source frontier differs from packaged frontier")
        print("empirical_rebuild: PASS")
    else:
        print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
