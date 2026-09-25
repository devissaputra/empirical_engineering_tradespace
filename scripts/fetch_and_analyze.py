#!/usr/bin/env python3
import csv,io,json,statistics,urllib.request
from research.model import pareto_front
URL='https://archive.ics.uci.edu/ml/machine-learning-databases/concrete/slump/slump_test.data'
raw=list(csv.DictReader(io.StringIO(urllib.request.urlopen(URL).read().decode('utf-8-sig'))))
rows=[{'experiment_id':int(float(r['No'])),'cement':float(r['Cement']),'slump_cm':float(r['SLUMP(cm)']),'strength_mpa':float(r['Compressive Strength (28-day)(Mpa)'])} for r in raw]
front=pareto_front(rows)
summary={'study':'Empirical Engineering Design Trade Space: Concrete Slump Experiments','headline_metrics':{'n_experiments':len(rows),'cement_mean':round(statistics.mean(r['cement'] for r in rows),2),'strength_mean_mpa':round(statistics.mean(r['strength_mpa'] for r in rows),2),'slump_mean_cm':round(statistics.mean(r['slump_cm'] for r in rows),2),'pareto_count':len(front),'pareto_fraction':round(len(front)/len(rows),3),'max_strength_mpa':max(r['strength_mpa'] for r in rows),'min_cement_kg_m3':min(r['cement'] for r in rows)},'finding':'Twenty-three of 103 observed experiments are non-dominated under the stated three-objective rule. The frontier includes both very high-strength mixes and much lower-cement mixes, so a single-score ranking would erase genuine trade-offs.','source':'UCI Concrete Slump Test','retrieved':'2026-09-25'}
print(json.dumps({'summary':summary,'frontier_experiment_ids':[r['experiment_id'] for r in front]},indent=2))
