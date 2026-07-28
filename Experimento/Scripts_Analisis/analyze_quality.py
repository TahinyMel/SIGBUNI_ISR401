#!/usr/bin/env python3
"""Análisis preliminar Enfoque 1: calidad RF humano vs LLM.

Uso (cuando existan datos reales):
  python3 analyze_quality.py --input ../Resultados/raw_scores.csv --out ../Resultados/
"""
from __future__ import annotations

import argparse
from pathlib import Path

import csv
import math
import statistics


def cohen_d(a: list[float], b: list[float]) -> float:
    if len(a) < 2 or len(b) < 2:
        return float("nan")
    na, nb = len(a), len(b)
    va, vb = statistics.variance(a), statistics.variance(b)
    pooled = math.sqrt(((na - 1) * va + (nb - 1) * vb) / (na + nb - 2))
    if pooled == 0:
        return 0.0
    return (statistics.mean(a) - statistics.mean(b)) / pooled


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    if not args.input.exists():
        raise SystemExit(
            f"No hay datos en {args.input}. No inventar resultados: "
            "ejecutar el experimento tras el registro OSF."
        )
    rows = list(csv.DictReader(args.input.open(encoding="utf-8")))
    human = [float(r["score"]) for r in rows if r["origin"] == "human"]
    llm = [float(r["score"]) for r in rows if r["origin"] == "llm"]
    args.out.mkdir(parents=True, exist_ok=True)
    out = args.out / "summary.csv"
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["group", "n", "mean", "stdev"])
        w.writerow(["human", len(human), statistics.mean(human), statistics.stdev(human) if len(human) > 1 else ""])
        w.writerow(["llm", len(llm), statistics.mean(llm), statistics.stdev(llm) if len(llm) > 1 else ""])
        w.writerow(["cohen_d_human_minus_llm", "", cohen_d(human, llm), ""])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
