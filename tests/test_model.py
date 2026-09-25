from research.model import (
    dominates,
    dominates_cement_strength,
    pareto_front,
    load_all_objectives,
    load_packaged_frontier,
    sensitivity_analysis,
    validate_bundle,
)

EXPECTED_FRONTIER_IDS = {
    4, 7, 8, 19, 25, 28, 33, 35, 36, 49, 50, 67, 68,
    83, 84, 88, 90, 97, 98, 100, 101, 102, 103,
}

EXPECTED_SENSITIVITY = {
    "baseline_three_objective": (103, 23, 1.000),
    "cement_strength_only": (103, 10, 0.435),
    "cement_strength_slump_ge_10": (84, 10, 0.435),
    "cement_strength_slump_ge_20": (63, 8, 0.348),
}

def test_dominance_direction():
    a = {"cement": 100, "slump_cm": 20, "strength_mpa": 40}
    b = {"cement": 120, "slump_cm": 18, "strength_mpa": 35}
    assert dominates(a, b)
    assert dominates_cement_strength(a, b)
    assert not dominates(b, a)

def test_frontier_fixture():
    a = {"cement": 100, "slump_cm": 20, "strength_mpa": 40}
    b = {"cement": 120, "slump_cm": 18, "strength_mpa": 35}
    c = {"cement": 80, "slump_cm": 10, "strength_mpa": 50}
    assert pareto_front([a, b, c]) == [a, c]

def test_complete_objective_table_has_all_103_observations():
    rows = load_all_objectives()
    assert len(rows) == 103
    assert {r["experiment_id"] for r in rows} == set(range(1, 104))

def test_recomputed_frontier_matches_packaged_frontier():
    all_rows = load_all_objectives()
    recomputed = pareto_front(all_rows)
    packaged = load_packaged_frontier()
    assert {r["experiment_id"] for r in recomputed} == EXPECTED_FRONTIER_IDS
    assert {r["experiment_id"] for r in packaged} == EXPECTED_FRONTIER_IDS

def test_sensitivity_specifications_are_reproducible():
    specs = {s["specification"]: s for s in sensitivity_analysis(load_all_objectives())}
    for name, (eligible_n, pareto_count, retention) in EXPECTED_SENSITIVITY.items():
        assert specs[name]["eligible_n"] == eligible_n
        assert specs[name]["pareto_count"] == pareto_count
        assert specs[name]["baseline_retention"] == retention

def test_full_bundle_validation():
    assert validate_bundle()
