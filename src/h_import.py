# -*- coding: utf-8 -*-
"""h_raw.json (72 tarif) + h_text.py -> rehberin kendi tarif biçimi.
- Malzemeler gram yerine adet / yk / tt / diş gibi mutfak ölçülerine çevrilir (ölçekleme için).
- Skyr -> protein quark (skyr de olur), eritritol -> stevia.
- Makrolar h_raw.json'daki hesaplanmış değerlerdir."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from h_text import T

RAW = json.load(open(os.path.join(HERE, "h_raw.json"), encoding="utf-8"))

# anahtar -> (birim, gram/birim)
UNIT = {
    "egg": ("adet", 50), "white": ("adet", 30), "ricepaper": ("yaprak", 9), "nori": ("yaprak", 3),
    "bread": ("dilim", 30), "tortilla": ("adet", 35), "banana": ("adet", 90), "apple": ("adet", 150),
    "garlic": ("diş", 3), "whey": ("ölçek", 30),
    "soy": ("yk", 15), "sriracha": ("yk", 15), "gochujang": ("yk", 15), "miso": ("yk", 15),
    "cocoa": ("yk", 7), "lemon": ("yk", 15), "lime": ("yk", 15),
    "sesameoil": ("tt", 5), "spice": ("tt", 3), "honey": ("tt", 6), "cinnamon": ("tt", 3),
    "vanilla": ("tt", 4), "mustard": ("tt", 6), "bakingpowder": ("tt", 6), "sesame": ("tt", 3),
}
NAME = {
    "egg": "Yumurta", "white": "Yumurta akı", "pepper": "Kapya biber", "turkey": "Hindi göğsü", "chicken": "Tavuk göğsü",
    "potato": "Patates", "shrimp": "Karides (ayıklanmış)", "salmon": "Somon", "squid": "Kalamar (ayıklanmış)",
    "beef": "Yağsız dana kıyma", "beefstrip": "Yağsız dana bonfile", "lamb": "Yağsız kuzu kıyma", "beefliver": "Dana ciğeri",
    "tuna": "Ton balığı (suda, süzülmüş)", "sardine": "Sardalya (suda, süzülmüş)", "rice": "Pirinç (pişmemiş)",
    "oats": "Yulaf ezmesi", "whey": "Whey protein (vanilya)", "lemon": "Limon suyu", "spice": "Baharat karışımı",
    "ricepaper": "Rice paper", "skyr": "Protein quark (veya skyr)", "erythritol": "Stevia (tatlandırıcı)",
    "edamame": "Edamame (haşlanmış)", "chickpeas": "Nohut (haşlanmış)", "lentils": "Yeşil mercimek (haşlanmış)",
}
GRP = {  # çipler ortak olsun
    "Yoğurt / skyr": "Yoğurt / quark", "Mozzarella": "Kaşar / mozzarella",
    "Ekmek / lavaş": "Ekmek / lavaş / tortilla", "Nohut": "Nohut / humus", "Ton balığı": "Balık",
}

def qty(key, g):
    if key in UNIT:
        u, per = UNIT[key]
        v = g / per
        if u in ("yk", "tt"):
            v = max(0.25, round(v * 4) / 4)
        elif u == "diş":
            v = max(1, round(v))
        elif u in ("yaprak",):
            v = max(1, round(v))
        else:
            v = round(v * 2) / 2
            if v == int(v):
                v = int(v)
        return v, u
    if key == "olive":
        return (round(g / 5 * 4) / 4, "tt") if g < 12 else (round(g / 14 * 4) / 4, "yk")
    return g, "g"

def clean(v):
    return int(v) if float(v) == int(v) else v

def norm(s):
    s = s.replace("İ", "i").replace("I", "ı").lower()
    for a, b in (("ı", "i"), ("ş", "s"), ("ğ", "g"), ("ü", "u"), ("ö", "o"), ("ç", "c")):
        s = s.replace(a, b)
    return s

def load():
    out = []
    for r in RAW:
        x = T[r["id"]]
        ing = []
        for i in r["ing"]:
            k = i["k"]
            name, q, u = NAME.get(k, i["name"]), None, None
            if k == "erythritol":
                q, u = 1, "tt"
            else:
                q, u = qty(k, i["g"])
            if k in x["ing"]:
                name, q, u = x["ing"][k]
            note = ""
            if k == "olive":
                name = "Zeytinyağı"
            ing.append(dict(k=k, name=name, grp=GRP.get(i["grp"], i["grp"]), q=clean(q), u=u, note=note))
        section = r["section"]
        kind = ""
        if section == "rice-nori":
            kind = "kahvaltı" if "kahvaltı" in r["kind"] else "akşam"
        elif section == "snack":
            kind = "tatlı" if r["kind"].startswith("Tatlı") else "tuzlu"
        title = x["title"] or r["title"]
        s = r["s"]
        grps = []
        for i in ing:
            if i["grp"] and i["grp"] not in grps:
                grps.append(i["grp"])
        cuisine = r["cuisine"]
        store = "" if r["storage"] == "Taze tüketim" else r["storage"]
        out.append(dict(
            id="H%d" % r["id"], section=section, kind=kind, title=title, cuisine=cuisine, time="%d dk" % r["time"],
            portion=x["portion"] or r["portion"].replace("Tencerenin / tepsinin üçte biri", "Tencerenin üçte biri"),
            s=dict(kcal=round(s["kcal"], 1), p=round(s["p"], 1), f=round(s["f"], 1), c=round(s["c"], 1),
                   g=round(s["raw_g"], 0), ratio=round(s["kcal"] / s["p"], 2)),
            ing=ing, steps=x["steps"], family=x["family"], swap=x["swap"], store=store, grps=grps,
            search=norm(" ".join([title, cuisine] + [i["name"] for i in ing]))))
    return out

if __name__ == "__main__":
    for r in load():
        print(r["id"], r["title"], r["time"], r["s"]["ratio"], [(i["q"], i["u"], i["name"]) for i in r["ing"]][:4])
