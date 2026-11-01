# -*- coding: utf-8 -*-
"""index.html'i tarayıcıda açıp temel akışı dener. Kullanım: python3 tools/smoke_test.py [ekran_goruntusu_klasoru]"""
import os, sys
from playwright.sync_api import sync_playwright
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
shots = sys.argv[1] if len(sys.argv) > 1 else None
errors = []
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1280, "height": 900})
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.on("console", lambda m: errors.append(m.text) if m.type == "error" and "net::ERR" not in m.text else None)
    pg.goto("file://" + os.path.join(ROOT, "index.html"))
    assert pg.locator(".card").count() == 112, pg.locator(".card").count()
    assert pg.locator(".card .pic svg").count() == 112
    # sekmeler
    pg.click('.tab[data-sec="snack"]'); assert pg.locator(".card").count() == 20
    pg.click('.tab[data-sec="all"]')
    # filtre: tavuk dahil, mantar hariç
    pg.click('.chip[data-grp="Tavuk"]'); n1 = pg.locator(".card").count()
    pg.click('.chip[data-grp="Mantar"]'); pg.click('.chip[data-grp="Mantar"]'); n2 = pg.locator(".card").count()
    assert 0 < n2 < n1, (n1, n2)
    pg.click("#reset")
    # kart aç + kişi sayısı
    pg.click('.card[data-id="H1"] [data-act="toggle"]')
    before = pg.locator('.card[data-id="H1"] .ing li').first.inner_text()
    pg.click('.card[data-id="H1"] [data-act="plus"]'); pg.click('.card[data-id="H1"] [data-act="plus"]')
    after = pg.locator('.card[data-id="H1"] .ing li').first.inner_text()
    assert before != after, (before, after)
    steps = pg.locator('.card[data-id="H1"] .steps li').count(); assert steps >= 4, steps
    # oyun
    pg.click('#g-meal [data-meal="kahvalti"]'); pg.click('#g-chips [data-ggrp="Yumurta"]'); pg.click("#g-go")
    pg.wait_for_selector("#g-result .game-result:not(.rolling) h3", timeout=5000)
    title = pg.locator("#g-result h3").inner_text(); assert title
    pg.click('[data-gact="open"]'); pg.wait_for_timeout(600)
    assert pg.locator(".card.open").count() >= 1
    if shots:
        os.makedirs(shots, exist_ok=True)
        pg.click("#reset"); pg.evaluate("window.scrollTo(0,0)")
        pg.screenshot(path=os.path.join(shots, "top.png"))
        pg.locator("#game").scroll_into_view_if_needed(); pg.screenshot(path=os.path.join(shots, "game.png"))
    b.close()
assert not errors, errors
print("OK: 112 tarif, filtre, ölçekleme, oyun çalışıyor; seçilen:", title)
