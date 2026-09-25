from research.model import dominates, pareto_front, load_packaged_frontier, validate_bundle
def test_dominance_direction():
    a={'cement':100,'slump_cm':20,'strength_mpa':40}; b={'cement':120,'slump_cm':18,'strength_mpa':35}; assert dominates(a,b); assert not dominates(b,a)
def test_frontier_fixture():
    a={'cement':100,'slump_cm':20,'strength_mpa':40}; b={'cement':120,'slump_cm':18,'strength_mpa':35}; c={'cement':80,'slump_cm':10,'strength_mpa':50}; assert pareto_front([a,b,c])==[a,c]
def test_full_packaged_frontier(): assert len(load_packaged_frontier())==23 and validate_bundle()
