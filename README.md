# 2027 Aile Tarif Rehberi

Yüksek protein, düşük kalorili, tüm ailenin birlikte yiyebileceği **112 tarif**. Tek dosyalık, bağımlılıksız bir web sayfası: `index.html` dosyasını çift tıklayıp açmak yeterli.

| Bölüm | Tarif |
|---|---|
| Kahvaltı | 29 |
| Akşam yemeği | 43 |
| Rice paper ve nori (kahvaltı + akşam) | 20 |
| Snack (tatlı + tuzlu) | 20 |

## Sayfada neler var

- **Kişi sayısı ayarı:** Tarifler 3 kişilik yazıldı. Üstteki ayar tüm tarifleri, kartın içindeki ayar sadece o tarifi değiştirir. Miktarlar mutfakta kullanışlı değerlere yuvarlanır (¼ yk, ½ adet gibi).
- **Makrolar:** Her tarifte porsiyon başına kalori, protein, karbonhidrat ve yağ ile önerilen porsiyon yazar.
- **★ yıldız:** Kalori / protein oranı en fazla 11 kcal/g olan ana tariflere verilir (hedef: 10 kcal ≈ 1 g protein). Snack'lerde protein hedefi yoktur, yıldız verilmez.
- **Malzemeye göre filtre:** Bir malzemeye dokununca içersin, ikinci dokunuşta içermesin, üçüncüde kalksın. "Hepsi olsun / Biri olsun" ve serbest metin arama var.
- **İllüstrasyon:** Her tarifin malzemelerine göre üretilen stilize tabak çizimi (fotoğraf değildir).
- **Bugün ne yesek?:** Sayfanın sonunda; öğünü ve evdeki malzemeleri seçince uygun bir tarifi rastgele seçer.

## Klasör yapısı

```
index.html          Üretilmiş sayfa (GitHub Pages bunu yayınlar)
src/
  data.py           40 tarif: malzeme besin tablosu (DB) + tarifler (R). Makrolar buradan hesaplanır
  compute.py        Makro ve oran hesabı, yıldız kuralı
  h_raw.json        72 tarif: hesaplanmış makrolar ve malzeme gramajları
  h_text.py         72 tarifin yapılışı, ortak sofra / bulamazsan notları, başlık değişiklikleri
  h_import.py       72 tarifi sayfa biçimine çevirir (gram -> adet / yk / tt, skyr -> quark, eritritol -> stevia)
  build.py          Hepsini birleştirip index.html üretir
  template.html     Sayfanın HTML, CSS ve JS kodu
tools/smoke_test.py Tarayıcıda hızlı uçtan uca test (playwright gerekir)
.github/workflows/pages.yml  GitHub Pages yayını
```

## Yeniden üretmek

Hiçbir pakete ihtiyaç yok, sadece Python 3:

```bash
python3 src/build.py
```

Bu komut `index.html` dosyasını baştan yazar.

## Tarif eklemek veya değiştirmek

**`src/data.py` (makrolar otomatik hesaplanır):** önce yeni malzeme gerekiyorsa `DB`'ye `I(ad, kategori, kcal, protein, yağ, karbonhidrat, birimler, grp)` ile ekle (değerler 100 g başına). Sonra `rec(...)` ile tarifi yaz. Malzemeler `(anahtar, miktar, birim, not)` biçimindedir ve miktar 3 kişilik içindir. Birimler: `g`, `ml`, `adet`, `yaprak`, `dilim`, `diş`, `ölçek`, `yk`, `tt`.

**72 tariflik grup:** Bu tariflerin makroları hazır geldi (`h_raw.json`). Metinleri `h_text.py` içinde `t(id, adımlar, ortak sofra, bulamazsan, ...)` ile düzenlenir. Malzeme birimleri `h_import.py` içindeki `UNIT` ve `NAME` sözlüklerinden gelir.

Sonra `python3 src/build.py` ve (isteğe bağlı) `python3 tools/smoke_test.py`.

## GitHub Pages ile yayınlamak

1. Repoyu GitHub'a gönder (`main` dalı).
2. **Settings → Pages → Build and deployment → Source: GitHub Actions** seç.
3. Her `main` push'unda `.github/workflows/pages.yml` sayfayı üretip yayınlar. Adres: `https://<kullanıcı>.github.io/<repo>/`

## Bilmen gerekenler

- Besin değerleri genel besin tablolarının ortalamasıdır; marka, pişirme ve porsiyon farkına göre yaklaşık ±%10 sapabilir.
- 72 tariflik grubun makroları skyr ile hesaplandı; protein quark yazıldı. İkisi birbirine çok yakın olduğu için değerler yeniden hesaplanmadı. Stevia da kaloriyi etkilemez.
- Whey'li tarifler kasıtlı olarak duruyor. Whey yoksa her tarifte "Bulamazsan" notunda alternatif yazar.
- Sayfa Google Fonts'tan iki yazı tipi yükler (Bricolage Grotesque, Figtree). İnternet yoksa sistem yazı tipine düşer, sayfa yine çalışır.
