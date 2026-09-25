from research.model import (
    dominates,
    pareto_front,
    load_all_objectives,
    load_packaged_frontier,
    validate_bundle,
)

EXPECTED_FRONTIER_IDS = {
    4, 7, 8, 19, 25, 28, 33, 35, 36, 49, 50, 67, 68,
    83, 84, 88, 90, 97, 98, 100, 101, 102, 103,
}

def test_dominance_direction():
    a = {"cement": 100, "slump_cm": 20, "strength_mpa": 40}
    b = {"cement": 120, "slump_cm": 18, "strength_mpa": 35}
    assert dominates(a, b)
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

def test_full_bundle_validation():
    assert validate_bundle()
