# -*- coding: utf-8 -*-
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import DB, R

BASE = 3

def grams(key, q, unit):
    d = DB[key]
    if unit in ("g", "ml"):
        return q
    if unit not in d["units"]:
        raise SystemExit("Birim yok: %s %s" % (key, unit))
    return q * d["units"][unit]

def calc(r):
    t = dict(kcal=0, p=0, f=0, c=0, g=0)
    for key, q, unit, note in r["ing"]:
        if key not in DB:
            raise SystemExit("Malzeme yok: " + key)
        g = grams(key, q, unit)
        d = DB[key]
        t["kcal"] += d["kcal"] * g / 100
        t["p"] += d["p"] * g / 100
        t["f"] += d["f"] * g / 100
        t["c"] += d["c"] * g / 100
        t["g"] += g
    s = {k: v / BASE for k, v in t.items()}
    s["ratio"] = s["kcal"] / s["p"] if s["p"] else 0
    return s

def star(r, s):
    if r["section"] == "snack":
        return False
    return 0 < s["ratio"] <= 11.0

if __name__ == "__main__":
    print("%-4s %-46s %5s %5s %5s %5s %6s %5s %s" % ("id", "tarif", "kcal", "P", "F", "C", "kcal/P", "g", "*"))
    for r in R:
        s = calc(r)
        print("%-4s %-46s %5.0f %5.1f %5.1f %5.1f %6.1f %5.0f %s" % (
            r["id"], r["title"][:46], s["kcal"], s["p"], s["f"], s["c"], s["ratio"], s["g"], "*" if star(r, s) else ""))
