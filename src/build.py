# -*- coding: utf-8 -*-
"""data.py (40 tarif, hesaplanır) + h_import.py (72 tarif) -> ../index.html"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data import DB, R
from compute import calc, star, BASE
import h_import

def norm(s):
    s = s.replace("İ", "i").replace("I", "ı").lower()
    for a, b in (("ı", "i"), ("ş", "s"), ("ğ", "g"), ("ü", "u"), ("ö", "o"), ("ç", "c")):
        s = s.replace(a, b)
    return s

# illüstrasyon için görsel etiketler (malzeme adlarından)
VIS = [
    ("poultry", ["tavuk", "hindi"]), ("meat", ["dana", "kuzu", "kiyma", "cigeri", "kofte", "bonfile"]),
    ("fish", ["somon", "balik", "levrek", "ton ", "sardalya", "morina"]), ("shrimp", ["karides", "kalamar"]),
    ("egg", ["yumurta"]), ("rice", ["pirinc", "pilav"]), ("potato", ["patates"]),
    ("bread", ["ekmek", "tortilla", "lavas", "yufka"]), ("ricepaper", ["rice paper"]), ("nori", ["nori"]),
    ("dairy", ["yogurt", "quark", "lor ", "labne", "cottage", "peynir", "kasar", "mozzarella"]),
    ("fruit", ["cilek", "mersin", "nar", "elma", "muz", "mango", "meyve"]), ("choc", ["kakao", "cikolata"]),
    ("legume", ["nohut", "mercimek", "edamame", "besan"]),
    ("green", ["ispanak", "marul", "maydanoz", "lahana", "brokoli", "roka", "dereotu", "feslegen", "kisnis", "kabak", "yesil"]),
    ("tomato", ["domates", "biber", "salsa", "passata"]), ("cuc", ["salatalik"]), ("eggplant", ["patlican"]),
    ("carrot", ["havuc"]), ("mushroom", ["mantar"]), ("lemon", ["limon", "lime"]),
]
def vis_tags(names):
    txt = " " + norm(" ".join(names)) + " "
    return [t for t, keys in VIS if any(k in txt for k in keys)]

recipes = []
for r in R:
    s = calc(r)
    ing, grps = [], []
    for key, q, unit, note in r["ing"]:
        d = DB[key]
        if note and norm(note) in norm(d["name"]):
            note = ""
        ing.append(dict(k=key, name=d["name"], grp=d["grp"], q=q, u=unit, note=note))
        if d["grp"] and d["grp"] not in grps:
            grps.append(d["grp"])
    search = norm(" ".join([r["title"], r["cuisine"]] + [i["name"] + " " + i["note"] for i in ing]))
    recipes.append(dict(
        id=r["id"], section=r["section"], kind=r["kind"], title=r["title"], cuisine=r["cuisine"], time=r["time"],
        portion=r["portion"], s=dict(kcal=s["kcal"], p=s["p"], f=s["f"], c=s["c"], g=s["g"], ratio=s["ratio"]),
        star=star(r, s), ing=ing, steps=r["steps"], family=r["family"], swap=r["swap"], store="", grps=grps, search=search))

for h in h_import.load():
    h["star"] = h["section"] != "snack" and 0 < h["s"]["ratio"] <= 11.0
    recipes.append(h)

for r in recipes:
    r["vis"] = vis_tags([i["name"] for i in r["ing"]] + [r["title"]])

ORDER = {"kahvalti": 0, "aksam": 1, "rice-nori": 2, "snack": 3}
recipes.sort(key=lambda r: (ORDER[r["section"]], 0 if not r["id"].startswith("H") else 1))

GROUPS = [
 ("Et ve balık", ["Tavuk", "Hindi", "Dana", "Kuzu", "Ciğer", "Balık", "Karides", "Kalamar"]),
 ("Yumurta ve süt ürünleri", ["Yumurta", "Whey", "Yoğurt / quark", "Lor / süzme peynir", "Beyaz peynir", "Kaşar / mozzarella", "Labne"]),
 ("Baklagil ve karbonhidrat", ["Nohut / humus", "Mercimek", "Edamame", "Pirinç", "Patates", "Ekmek / lavaş / tortilla", "Rice paper", "Nori"]),
 ("Sebze", ["Patlıcan", "Kabak", "Ispanak", "Brokoli", "Mantar", "Lahana", "Domates", "Avokado"]),
]
chipGroups = []
for label, names in GROUPS:
    chips = [dict(grp=g, n=sum(1 for r in recipes if g in r["grps"])) for g in names]
    chipGroups.append(dict(label=label, chips=[c for c in chips if c["n"]]))

data = dict(base=BASE, recipes=recipes, chipGroups=chipGroups)
tpl = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
out = tpl.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
dst = os.path.join(HERE, "..", "index.html")
open(dst, "w", encoding="utf-8").write(out)
print("yazıldı", os.path.normpath(dst), len(out) // 1024, "KB;", len(recipes), "tarif;", sum(r["star"] for r in recipes), "yıldızlı")
