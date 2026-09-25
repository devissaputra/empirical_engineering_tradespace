#!/usr/bin/env python3
from __future__ import annotations
import argparse
import csv
import html
import json
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

def load_rows():
    with (ROOT / "data/derived/objective_observations.csv").open(encoding="utf-8") as f:
        return [
            {
                "experiment_id": int(r["experiment_id"]),
                "cement": float(r["cement"]),
                "slump_cm": float(r["slump_cm"]),
                "strength_mpa": float(r["strength_mpa"]),
            }
            for r in csv.DictReader(f)
        ]

def load_frontier_ids():
    with (ROOT / "data/derived/primary_results.csv").open(encoding="utf-8") as f:
        return {int(r["experiment_id"]) for r in csv.DictReader(f)}

def load_summary():
    return json.loads((ROOT / "results/empirical_summary.json").read_text(encoding="utf-8"))

def load_sensitivity():
    return json.loads((ROOT / "results/sensitivity_summary.json").read_text(encoding="utf-8"))

def svg_open(w, h):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>'

def text(x, y, value, size=16, weight="400", anchor="start"):
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(str(value))}</text>'

def box(x, y, w, h, title, body):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#f7f7f7" stroke="#333"/>'
        + text(x + w/2, y + 34, title, 17, "700", "middle")
        + text(x + w/2, y + 63, body, 14, "400", "middle")
    )

def architecture():
    s = [svg_open(1200, 430), text(50, 55, "Empirical Engineering Trade Space", 29, "700"),
         text(50, 88, "Public data → explicit objectives → Pareto frontier → sensitivity analysis → bounded interpretation", 16)]
    xs = [30, 260, 490, 720, 950]
    titles = ["Source", "Scope", "Baseline", "Robustness", "Interpret"]
    bodies = ["UCI slump data", "103 experiments", "23-point frontier", "4 specifications", "Bounded claim"]
    for i, x in enumerate(xs):
        s.append(box(x, 145, 190, 135, titles[i], bodies[i]))
        if i < 4:
            s.append(f'<line x1="{x+190}" y1="212" x2="{xs[i+1]-12}" y2="212" stroke="#222" stroke-width="2.5"/>')
    s.append("</svg>")
    return "".join(s)

def method():
    steps = [
        ("1 • Public source", ["UCI Concrete Slump Test", "103 laboratory experiments", "DOI 10.24432/C5FG7D"]),
        ("2 • Validate evidence", ["Parse source variables", "Check released metrics", "Record source SHA 256"]),
        ("3 • Objective table", ["Cement • minimize", "Slump • baseline maximize", "28 day strength • maximize"]),
    ]
    def tx(x, y, value, size=16, weight="400", anchor="start", fill="#172033"):
        return (
            f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">'
            f'{html.escape(str(value))}</text>'
        )
    def rect_box(x, y, w, h, title, lines, fill="#f8fafc", stroke="#94a3b8"):
        out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="15" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>',
               tx(x+18, y+31, title, 16, "700")]
        out.extend(tx(x+18, y+57+i*22, line, 12.5, "400", "start", "#475569") for i, line in enumerate(lines))
        return "".join(out)
    def arrow(x1, y1, x2, y2):
        return (
            f'<line x1="{x1}" y1="{y1}" x2="{x2-12}" y2="{y2}" stroke="#475569" stroke-width="2"/>'
            f'<polygon points="{x2-12},{y2-6} {x2},{y2} {x2-12},{y2+6}" fill="#475569"/>'
        )

    s = [svg_open(1200, 700),
         tx(55, 52, "Reproducible analysis pipeline", 30, "700"),
         tx(55, 82, "From public evidence to baseline frontier, operationalization sensitivity, and bounded engineering interpretation", 15, "400", "start", "#475569")]

    colors = [("#eff6ff", "#60a5fa"), ("#f8fafc", "#94a3b8"), ("#f8fafc", "#94a3b8")]
    xs = [45, 290, 535]
    for (title, lines), x, (fill, stroke) in zip(steps, xs, colors):
        s.append(rect_box(x, 125, 205, 130, title, lines, fill, stroke))
    s += [arrow(250,190,290,190), arrow(495,190,535,190),
          '<line x1="740" y1="190" x2="785" y2="190" stroke="#475569" stroke-width="2"/>',
          '<line x1="785" y1="190" x2="785" y2="338" stroke="#475569" stroke-width="2"/>',
          '<line x1="785" y1="190" x2="785" y2="510" stroke="#475569" stroke-width="2"/>',
          '<polygon points="773,332 785,338 773,344" fill="#475569"/>',
          '<polygon points="773,504 785,510 773,516" fill="#475569"/>',
          rect_box(815,275,330,145,"4A • Baseline frontier",["Exact pairwise Pareto dominance","All 103 observations eligible","23 efficient observations • 22.3%"],"#fff7ed","#fb923c"),
          rect_box(815,447,330,145,"4B • Sensitivity frontiers",["Omit slump objective → 10","Slump ≥ 10 cm → 10","Slump ≥ 20 cm → 8"],"#f0fdf4","#4ade80"),
          rect_box(45,320,280,145,"5 • Stability metrics",["Frontier size","Baseline overlap and retention","Jaccard similarity • exact IDs"]),
          rect_box(365,320,360,145,"6 • Evidence integrity",["Offline recomputation from packaged table","Internet rebuild against public UCI source","Tests + hashes + deterministic figures"]),
          arrow(815,348,725,392), arrow(815,520,725,420), arrow(325,392,365,392),
          rect_box(250,525,475,120,"7 • Interpretation boundary",["Frontier membership is conditional on the declared decision model.","No field ready concrete recommendation is inferred."],"#fef2f2","#f87171"),
          arrow(545,465,545,525),
          tx(55,680,"Key design principle: hold the observations fixed, change only the role of slump, then quantify how the efficient set changes.",13,"600","start","#334155"),
          "</svg>"]
    return "".join(s)

def evaluation():
    summary = load_summary()
    finding = summary["finding"]
    boundary = (
        "Observed frontiers depend on the declared objectives. The sensitivity thresholds are analytical checks, "
        "not universal concrete-design requirements; durability, cost, safety, and uncertainty remain outside this model."
    )
    s = [svg_open(1200, 520), text(50, 55, "Empirical Engineering Trade Space — Evidence Boundary", 29, "700"),
         box(55, 105, 1090, 140, "Empirical finding", finding),
         box(55, 285, 1090, 140, "Claim boundary", boundary),
         "</svg>"]
    return "".join(s)

def research_design():
    rows = load_rows()
    frontier = load_frontier_ids()
    w, h = 1200, 720
    left, right, top, bottom = 105, 835, 125, 610
    xmin, xmax, ymin, ymax = 130, 380, 15, 60

    def sx(v):
        return left + (v-xmin)/(xmax-xmin)*(right-left)

    def sy(v):
        return bottom - (v-ymin)/(ymax-ymin)*(bottom-top)

    def tx(x, y, value, size=16, weight="400", anchor="start", fill="#172033"):
        return (
            f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">'
            f'{html.escape(str(value))}</text>'
        )

    s = [svg_open(w, h),
         tx(55,52,"Observed engineering trade space",30,"700"),
         tx(55,82,"103 laboratory mixtures from UCI Concrete Slump Test • bubble size = slump • orange ring = baseline Pareto efficient",15,"400","start","#475569")]

    for x in [150,200,250,300,350]:
        xx = sx(x)
        s.append(f'<line x1="{xx}" y1="{top}" x2="{xx}" y2="{bottom}" stroke="#e2e8f0"/>')
        s.append(tx(xx,bottom+28,x,13,"400","middle","#475569"))
    for y in [20,30,40,50,60]:
        yy = sy(y)
        s.append(f'<line x1="{left}" y1="{yy}" x2="{right}" y2="{yy}" stroke="#e2e8f0"/>')
        s.append(tx(left-16,yy+5,y,13,"400","end","#475569"))

    s += [f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#334155" stroke-width="1.8"/>',
          f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#334155" stroke-width="1.8"/>',
          tx((left+right)/2,680,"Cement content (kg/m³) — lower is preferred in the decision model",15,"600","middle"),
          f'<text x="28" y="{(top+bottom)/2}" transform="rotate(-90 28 {(top+bottom)/2})" font-family="Arial, Helvetica, sans-serif" font-size="15" font-weight="600" text-anchor="middle" fill="#172033">28 day compressive strength (MPa) — higher is preferred</text>']

    for r in rows:
        rad = 4 + max(r["slump_cm"],0)/6
        is_front = r["experiment_id"] in frontier
        s.append(
            f'<circle cx="{sx(r["cement"]):.2f}" cy="{sy(r["strength_mpa"]):.2f}" r="{rad:.2f}" '
            f'fill="{"#f59e0b" if is_front else "#2563eb"}" fill-opacity="{"0.62" if is_front else "0.28"}" '
            f'stroke="{"#b45309" if is_front else "#1d4ed8"}" stroke-width="{"2.1" if is_front else "0.7"}"/>'
        )

    annotations = [
        (35,18,-18,"ID 35 • 137 kg/m³ • 34.45 MPa • slump 27.5","start"),
        (49,15,-18,"ID 49 • max strength 58.53 MPa","start"),
        (103,-18,28,"ID 103 • slump 29 cm • 48.77 MPa","end"),
    ]
    by_id = {r["experiment_id"]: r for r in rows}
    for eid, dx, dy, label, anchor in annotations:
        r = by_id[eid]
        x, y = sx(r["cement"]), sy(r["strength_mpa"])
        s.append(f'<line x1="{x}" y1="{y}" x2="{x+dx*0.72}" y2="{y+dy*0.72}" stroke="#64748b" stroke-width="1.2"/>')
        s.append(tx(x+dx,y+dy,label,12,"600",anchor,"#334155"))

    s += ['<rect x="875" y="125" width="270" height="315" rx="16" fill="#f8fafc" stroke="#cbd5e1"/>',
          tx(900,160,"How to read the figure",18,"700"),
          '<circle cx="910" cy="196" r="7" fill="#2563eb" fill-opacity="0.28" stroke="#1d4ed8" stroke-width="0.7"/>',
          tx(930,201,"Observed mixture",13),
          '<circle cx="910" cy="232" r="8" fill="#f59e0b" fill-opacity="0.62" stroke="#b45309" stroke-width="2.1"/>',
          tx(930,237,"Baseline Pareto efficient",13),
          tx(900,282,"Bubble size encodes slump",13,"600")]

    for cy, slump in [(315,0),(350,15),(390,30)]:
        rad = 4 + slump/6
        s.append(f'<circle cx="925" cy="{cy}" r="{rad}" fill="#94a3b8" fill-opacity="0.38" stroke="#64748b"/>')
        s.append(tx(950,cy+5,f"{slump} cm",12))

    s += ['<rect x="875" y="462" width="270" height="148" rx="16" fill="#fff7ed" stroke="#fdba74"/>',
          tx(900,494,"Scientific caution",15,"700","start","#9a3412"),
          tx(900,522,"This is a 2D projection.",12,"600","start","#7c2d12"),
          tx(900,546,"Baseline dominance also uses slump,",12,"400","start","#7c2d12"),
          tx(900,568,"so ringed points need not form a",12,"400","start","#7c2d12"),
          tx(900,590,"simple 2D frontier in this view.",12,"400","start","#7c2d12"),
          tx(55,708,"Baseline objective directions: minimize cement; maximize slump; maximize 28 day compressive strength.",12,"400","start","#64748b"),
          "</svg>"]
    return "".join(s)

def sensitivity():
    specs = load_sensitivity()["specifications"]
    labels = {
        "baseline_three_objective": "Baseline: 3 objectives",
        "cement_strength_only": "Cement + strength",
        "cement_strength_slump_ge_10": "Slump ≥10 cm",
        "cement_strength_slump_ge_20": "Slump ≥20 cm",
    }
    w, h = 1100, 560
    left, top, bottom = 110, 100, 470
    max_count = max(s["pareto_count"] for s in specs)
    bar_w = 150
    gap = 70
    s = [svg_open(w, h), text(50, 48, "Sensitivity of the observed Pareto decision set", 28, "700"),
         text(50, 76, "Alternative operationalizations test dependence on treating slump as an optimization objective.", 15)]
    for i, spec in enumerate(specs):
        x = left + i*(bar_w+gap)
        bh = (spec["pareto_count"]/max_count)*(bottom-top)
        y = bottom-bh
        s.append(f'<rect x="{x}" y="{y:.2f}" width="{bar_w}" height="{bh:.2f}" fill="#555" fill-opacity="0.72"/>')
        s.append(text(x+bar_w/2, y-12, spec["pareto_count"], 18, "700", "middle"))
        s.append(text(x+bar_w/2, bottom+28, labels[spec["specification"]], 13, "700", "middle"))
        s.append(text(x+bar_w/2, bottom+50, f'baseline retention {spec["baseline_retention"]:.3f}', 12, "400", "middle"))
    s.append(f'<line x1="{left-20}" y1="{bottom}" x2="1040" y2="{bottom}" stroke="#222"/>')
    s.append(text(50, 550, "Thresholds are analytical sensitivity checks, not universal engineering requirements.", 13))
    s.append("</svg>")
    return "".join(s)

def render_all(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    figures = {
        "architecture.svg": architecture(),
        "method.svg": method(),
        "evaluation.svg": evaluation(),
        "research_design.svg": research_design(),
        "sensitivity.svg": sensitivity(),
    }
    for name, content in figures.items():
        path = out_dir / name
        path.write_text(content, encoding="utf-8")
        ET.fromstring(content)
    return figures

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(ROOT / "assets"))
    args = parser.parse_args()
    figures = render_all(Path(args.out_dir))
    print(f"generated_figures: {len(figures)}")

if __name__ == "__main__":
    main()
