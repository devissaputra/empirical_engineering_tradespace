from __future__ import annotations
import csv
import hashlib
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

def dominates_cement_strength(a, b):
    return (
        a["cement"] <= b["cement"]
        and a["strength_mpa"] >= b["strength_mpa"]
        and (
            a["cement"] < b["cement"]
            or a["strength_mpa"] > b["strength_mpa"]
        )
    )

def pareto_front(rows, dominance=dominates):
    return [
        b for i, b in enumerate(rows)
        if not any(j != i and dominance(a, b) for j, a in enumerate(rows))
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

def load_sensitivity_summary():
    return json.loads((ROOT / "results/sensitivity_summary.json").read_text(encoding="utf-8"))

def sensitivity_analysis(rows):
    baseline = pareto_front(rows, dominates)
    specs = [
        ("baseline_three_objective", rows, dominates,
         "Minimize cement; maximize slump and 28-day strength."),
        ("cement_strength_only", rows, dominates_cement_strength,
         "Minimize cement and maximize 28-day strength; slump is not an objective."),
        ("cement_strength_slump_ge_10", [r for r in rows if r["slump_cm"] >= 10], dominates_cement_strength,
         "Minimize cement and maximize strength among observations with slump >= 10 cm."),
        ("cement_strength_slump_ge_20", [r for r in rows if r["slump_cm"] >= 20], dominates_cement_strength,
         "Minimize cement and maximize strength among observations with slump >= 20 cm."),
    ]
    baseline_ids = {r["experiment_id"] for r in baseline}
    output = []
    for name, eligible, dominance, description in specs:
        front = pareto_front(eligible, dominance)
        front_ids = {r["experiment_id"] for r in front}
        union = baseline_ids | front_ids
        output.append({
            "specification": name,
            "description": description,
            "eligible_n": len(eligible),
            "pareto_count": len(front),
            "frontier_ids": sorted(front_ids),
            "baseline_overlap_count": len(baseline_ids & front_ids),
            "baseline_retention": round(len(baseline_ids & front_ids) / len(baseline_ids), 3),
            "jaccard_with_baseline": round(len(baseline_ids & front_ids) / len(union), 3),
        })
    return output

def _sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def validate_bundle():
    summary = load_summary()
    all_rows = load_all_objectives()
    packaged = load_packaged_frontier()
    recomputed = pareto_front(all_rows)
    expected_ids = {r["experiment_id"] for r in packaged}
    recomputed_ids = {r["experiment_id"] for r in recomputed}
    sensitivity = load_sensitivity_summary()
    recalculated_sensitivity = sensitivity_analysis(all_rows)
    manifest = json.loads((ROOT / "data/source_manifest.json").read_text(encoding="utf-8"))
    integrity = manifest["integrity"]
    return (
        len(all_rows) == summary["headline_metrics"]["n_experiments"] == 103
        and len(packaged) == summary["headline_metrics"]["pareto_count"] == 23
        and expected_ids == recomputed_ids
        and round(len(recomputed) / len(all_rows), 3)
        == summary["headline_metrics"]["pareto_fraction"]
        and sensitivity["specifications"] == recalculated_sensitivity
        and _sha256(ROOT / "data/derived/objective_observations.csv")
        == integrity["objective_observations_sha256"]
        and _sha256(ROOT / "data/derived/sensitivity_results.csv")
        == integrity["sensitivity_results_sha256"]
    )
