from __future__ import annotations
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def dominates(a,b):
    return (a['cement']<=b['cement'] and a['slump_cm']>=b['slump_cm'] and a['strength_mpa']>=b['strength_mpa'] and (a['cement']<b['cement'] or a['slump_cm']>b['slump_cm'] or a['strength_mpa']>b['strength_mpa']))
def pareto_front(rows): return [b for i,b in enumerate(rows) if not any(j!=i and dominates(a,b) for j,a in enumerate(rows))]
def load_packaged_frontier():
    with (ROOT/'data/derived/primary_results.csv').open() as f:
        out=[]
        for r in csv.DictReader(f): out.append({k:(float(v) if k!='experiment_id' else int(v)) for k,v in r.items()})
        return out
def load_summary(): return json.loads((ROOT/'results/empirical_summary.json').read_text())
def validate_bundle():
    s=load_summary(); f=load_packaged_frontier()
    return len(f)==s['headline_metrics']['pareto_count']==23 and all(not dominates(a,b) for i,b in enumerate(f) for j,a in enumerate(f) if i!=j)
