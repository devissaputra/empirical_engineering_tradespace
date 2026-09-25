from __future__ import annotations
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def dominates(a, b):
    return (
        a["cement"] <= b["cement"]
        and a["slump_cm"] >= b["slump_cm"]
        and a["strength_mpa"] >= b["strength_mpa"]
        and (
            a["cement"] < b["cement"]
            or a["slump_cm"] > b["slump_cm"]
            or a["strength_mpa"] > b["strength_mpa"]
        )
    )

def pareto_front(rows):
    return [
        b for i, b in enumerate(rows)
        if not any(j != i and dominates(a, b) for j, a in enumerate(rows))
    ]

def _load_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        out = []
        for r in csv.DictReader(f):
            out.append({
                "experiment_id": int(r["experiment_id"]),
                "cement": float(r["cement"]),
                "slump_cm": float(r["slump_cm"]),
                "strength_mpa": float(r["strength_mpa"]),
            })
        return out

def load_all_objectives():
    return _load_csv(ROOT / "data/derived/objective_observations.csv")

def load_packaged_frontier():
    return _load_csv(ROOT / "data/derived/primary_results.csv")

def load_summary():
    return json.loads((ROOT / "results/empirical_summary.json").read_text(encoding="utf-8"))

def validate_bundle():
    summary = load_summary()
    all_rows = load_all_objectives()
    packaged = load_packaged_frontier()
    recomputed = pareto_front(all_rows)
    expected_ids = {r["experiment_id"] for r in packaged}
    recomputed_ids = {r["experiment_id"] for r in recomputed}
    return (
        len(all_rows) == summary["headline_metrics"]["n_experiments"] == 103
        and len(packaged) == summary["headline_metrics"]["pareto_count"] == 23
        and expected_ids == recomputed_ids
        and round(len(recomputed) / len(all_rows), 3)
        == summary["headline_metrics"]["pareto_fraction"]
    )
