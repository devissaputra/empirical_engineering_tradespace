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
         text(50, 88, "Public data → explicit objectives → Pareto frontier → bounded interpretation", 16)]
    xs = [40, 275, 510, 745, 980]
    titles = ["Source", "Scope", "Analysis", "Evidence", "Interpret"]
    bodies = ["UCI slump data", "103 experiments", "Pareto rule", "23 frontier points", "Bounded claim"]
    for i, x in enumerate(xs):
        s.append(box(x, 145, 180, 135, titles[i], bodies[i]))
        if i < 4:
            s.append(f'<line x1="{x+180}" y1="212" x2="{xs[i+1]-12}" y2="212" stroke="#222" stroke-width="2.5"/>')
    s.append("</svg>")
    return "".join(s)

def method():
    steps = [
        "Load all 103 observed experiments.",
        "Minimize cement; maximize slump and 28-day strength.",
        "Apply pairwise Pareto dominance to the full observed set.",
        "Report the complete non-dominated decision set, not one universal optimum.",
    ]
    s = [svg_open(1200, 520), text(50, 55, "Empirical Engineering Trade Space — Method", 29, "700"),
         text(50, 88, "The frontier is recomputed from all 103 packaged objective observations.", 16)]
    for i, step in enumerate(steps, 1):
        y = 130 + (i-1)*88
        s.append(f'<circle cx="82" cy="{y+35}" r="24" fill="#f0f0f0" stroke="#222"/>')
        s.append(text(82, y+42, i, 17, "700", "middle"))
        s.append(f'<rect x="125" y="{y}" width="1000" height="70" rx="12" fill="#f8f8f8" stroke="#444"/>')
        s.append(text(150, y+42, step, 16))
    s.append("</svg>")
    return "".join(s)

def evaluation():
    summary = load_summary()
    finding = summary["finding"]
    boundary = (
        "Empirical trade-space demonstration only: application-specific constraints, durability, "
        "cost, safety, and uncertainty are outside this model."
    )
    s = [svg_open(1200, 520), text(50, 55, "Empirical Engineering Trade Space — Evidence Boundary", 29, "700"),
         box(55, 105, 1090, 140, "Empirical finding", finding),
         box(55, 285, 1090, 140, "Claim boundary", boundary),
         "</svg>"]
    return "".join(s)

def research_design():
    rows = load_rows()
    frontier = load_frontier_ids()
    w, h = 1100, 620
    left, right, top, bottom = 90, 1040, 90, 535
    xmin, xmax = min(r["cement"] for r in rows), max(r["cement"] for r in rows)
    ymin, ymax = min(r["strength_mpa"] for r in rows), max(r["strength_mpa"] for r in rows)
    def sx(v): return left + (v-xmin)/(xmax-xmin)*(right-left)
    def sy(v): return bottom - (v-ymin)/(ymax-ymin)*(bottom-top)
    s = [svg_open(w, h), text(50, 48, "Observed engineering trade space", 28, "700"),
         text(50, 76, "Cement vs 28-day strength; point size reflects slump. Frontier points are ringed.", 15),
         f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="#222"/>',
         f'<line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="#222"/>']
    for r in rows:
        x, y = sx(r["cement"]), sy(r["strength_mpa"])
        rad = 2.5 + max(r["slump_cm"], 0)/9
        fill = "#555" if r["experiment_id"] not in frontier else "#111"
        stroke = "#111" if r["experiment_id"] in frontier else "none"
        sw = 2.2 if r["experiment_id"] in frontier else 0
        s.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{rad:.2f}" fill="{fill}" fill-opacity="0.55" stroke="{stroke}" stroke-width="{sw}"/>')
    s += [text((left+right)/2, 585, "Cement (kg/m³)", 16, "400", "middle"),
          f'<text x="25" y="{(top+bottom)/2}" transform="rotate(-90 25 {(top+bottom)/2})" font-family="Arial, sans-serif" font-size="16" text-anchor="middle">28-day compressive strength (MPa)</text>',
          text(835, 112, "Ringed = Pareto-efficient", 14, "700"), "</svg>"]
    return "".join(s)

def render_all(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    figures = {
        "architecture.svg": architecture(),
        "method.svg": method(),
        "evaluation.svg": evaluation(),
        "research_design.svg": research_design(),
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
