# -*- coding: utf-8 -*-
# Besin veritabanı: 100 g başına kcal, protein, yağ, karbonhidrat
def I(name, cat, kcal, p, f, c, units=None, grp=None):
    return dict(name=name, cat=cat, kcal=kcal, p=p, f=f, c=c, units=units or {}, grp=grp)

DB = {
 # proteinler
 "tavuk_gogsu": I("Tavuk göğsü", "protein", 120, 22.5, 2.6, 0, grp="Tavuk"),
 "tavuk_but": I("Tavuk but (derisiz, kemiksiz)", "protein", 125, 19.5, 4.5, 0, grp="Tavuk"),
 "hindi_gogus_kiyma": I("Hindi göğüs kıyma", "protein", 115, 23, 2, 0, grp="Hindi"),
 "hindi_fume": I("Hindi füme (dilim)", "protein", 105, 17, 2.5, 2, grp="Hindi"),
 "dana_kiyma": I("Az yağlı dana kıyma", "protein", 137, 21.4, 5, 0, grp="Dana"),
 "dana_bonfile": I("Dana bonfile", "protein", 125, 22, 3.5, 0, grp="Dana"),
 "kuzu_kiyma": I("Yağsız kuzu kıyma", "protein", 140, 21, 5.5, 0, grp="Kuzu"),
 "dana_cigeri": I("Dana ciğeri", "protein", 135, 20.4, 3.6, 3.9, grp="Ciğer"),
 "levrek": I("Levrek fileto", "protein", 97, 18.4, 2, 0, grp="Balık"),
 "somon": I("Somon fileto", "protein", 208, 20, 13, 0, grp="Balık"),
 "fume_somon": I("Füme somon", "protein", 117, 18, 4.3, 0, grp="Balık"),
 "karides": I("Karides (soyulmuş)", "protein", 85, 20, 0.5, 0, grp="Karides"),
 "yumurta": I("Yumurta", "protein", 143, 12.6, 9.5, 0.7, {"adet": 50}, grp="Yumurta"),
 "yumurta_aki": I("Yumurta akı", "protein", 52, 10.9, 0.2, 0.7, {"adet": 33}, grp="Yumurta"),
 "whey": I("Whey protein (vanilya)", "protein", 400, 80, 6, 8, {"ölçek": 30}, grp="Whey"),
 "whey_cikolata": I("Whey protein (çikolata)", "protein", 395, 78, 6, 8, {"ölçek": 30}, grp="Whey"),
 # süt ürünleri
 "suzme_yogurt": I("Süzme yoğurt (%2)", "sut", 70, 9.5, 2, 4, grp="Yoğurt / quark"),
 "yogurt": I("Yoğurt (az yağlı)", "sut", 45, 4.5, 1.5, 5, grp="Yoğurt / quark"),
 "lor": I("Lor peyniri", "sut", 85, 12, 3, 3, grp="Lor / süzme peynir"),
 "suzme_peynir": I("Süzme peynir (cottage)", "sut", 82, 11, 2.3, 3.4, grp="Lor / süzme peynir"),
 "beyaz_peynir": I("Beyaz peynir (light)", "sut", 180, 18, 11, 2, grp="Beyaz peynir"),
 "mozzarella": I("Mozzarella (light)", "sut", 190, 22, 10, 2, grp="Kaşar / mozzarella"),
 "kasar": I("Kaşar (light)", "sut", 240, 28, 13, 1.5, grp="Kaşar / mozzarella"),
 "labne": I("Labne (light)", "sut", 120, 8, 7, 5, grp="Labne"),
 "sut": I("Süt (yarım yağlı)", "sut", 50, 3.4, 1.8, 4.8),
 # baklagil
 "nohut": I("Nohut (haşlanmış)", "baklagil", 164, 8.9, 2.6, 27.4, grp="Nohut / humus"),
 "nohut_unu": I("Nohut unu", "baklagil", 387, 22, 6.7, 58, grp="Nohut / humus"),
 "humus": I("Humus", "baklagil", 166, 8, 9.6, 14, grp="Nohut / humus"),
 "mercimek": I("Kırmızı mercimek (kuru)", "baklagil", 350, 25, 1.1, 60, grp="Mercimek"),
 "edamame": I("Edamame", "baklagil", 121, 11.9, 5.2, 8.9, grp="Edamame"),
 # karbonhidrat
 "pilav": I("Pirinç (pişmiş)", "karb", 130, 2.7, 0.3, 28, grp="Pirinç"),
 "sushi_pirinc": I("Sushi pirinci (pişmiş)", "karb", 130, 2.4, 0.2, 29, grp="Pirinç"),
 "pirinc_kuru": I("Pirinç (kuru)", "karb", 360, 6.7, 0.6, 79, grp="Pirinç"),
 "patates": I("Patates", "karb", 77, 2, 0.1, 17.5, grp="Patates"),
 "ekmek": I("Tam buğday ekmek", "karb", 250, 12, 3, 44, {"dilim": 30}, grp="Ekmek / lavaş / tortilla"),
 "lavas": I("Lavaş", "karb", 275, 9, 1.5, 56, {"adet": 60}, grp="Ekmek / lavaş / tortilla"),
 "tortilla": I("Tam buğday tortilla (küçük)", "karb", 310, 9, 8, 50, {"adet": 30}, grp="Ekmek / lavaş / tortilla"),
 "tb_un": I("Tam buğday unu", "karb", 340, 13, 2.5, 72, {"yk": 10}),
 "rice_paper": I("Rice paper", "karb", 335, 1.5, 0.3, 80, {"yaprak": 9}, grp="Rice paper"),
 "nori": I("Nori", "karb", 300, 36, 2, 38, {"yaprak": 3}, grp="Nori"),
 # sebze
 "domates": I("Domates", "sebze", 18, 0.9, 0.2, 3.9),
 "salatalik": I("Salatalık", "sebze", 15, 0.7, 0.1, 3.6),
 "yesil_biber": I("Yeşil biber", "sebze", 20, 0.9, 0.2, 4.6),
 "kirmizi_biber": I("Kırmızı biber", "sebze", 31, 1, 0.3, 6),
 "sogan": I("Soğan", "sebze", 40, 1.1, 0.1, 9.3),
 "sarimsak": I("Sarımsak", "sebze", 149, 6.4, 0.5, 33, {"diş": 4}),
 "patlican": I("Patlıcan", "sebze", 25, 1, 0.2, 6, grp="Patlıcan"),
 "kabak": I("Kabak", "sebze", 17, 1.2, 0.3, 3.1, grp="Kabak"),
 "ispanak": I("Ispanak", "sebze", 23, 2.9, 0.4, 3.6, grp="Ispanak"),
 "brokoli": I("Brokoli", "sebze", 34, 2.8, 0.4, 7, grp="Brokoli"),
 "havuc": I("Havuç", "sebze", 41, 0.9, 0.2, 9.6),
 "mantar": I("Mantar", "sebze", 22, 3.1, 0.3, 3.3, grp="Mantar"),
 "lahana": I("Lahana", "sebze", 25, 1.3, 0.1, 5.8),
 "avokado": I("Avokado", "sebze", 160, 2, 15, 9, grp="Avokado"),
 "yesil_sogan": I("Yeşil soğan", "sebze", 32, 1.8, 0.2, 7.3),
 "zencefil": I("Taze zencefil", "sebze", 80, 1.8, 0.8, 18),
 "taze_ot": I("Taze otlar", "sebze", 36, 3, 0.8, 6),
 "limon": I("Limon suyu", "sebze", 22, 0.4, 0.2, 6.9, {"adet": 30}),
 "zeytin": I("Zeytin", "sebze", 145, 1, 15, 4),
 # meyve
 "elma": I("Elma", "meyve", 52, 0.3, 0.2, 14, {"adet": 150}),
 "cilek": I("Çilek", "meyve", 32, 0.7, 0.3, 7.7),
 "yaban_mersini": I("Yaban mersini", "meyve", 57, 0.7, 0.3, 14),
 "nar": I("Nar", "meyve", 83, 1.7, 1.2, 19),
 "mango": I("Mango (dondurulmuş)", "meyve", 60, 0.8, 0.4, 15),
 # yağ, sos, diğer
 "zeytinyagi": I("Zeytinyağı", "diger", 884, 0, 100, 0, {"yk": 13.5, "tt": 4.5}),
 "susam_yagi": I("Susam yağı", "diger", 884, 0, 100, 0, {"yk": 13.5, "tt": 4.5}),
 "ceviz": I("Ceviz içi", "diger", 654, 15, 65, 14),
 "bal": I("Bal", "diger", 304, 0.3, 0, 82, {"yk": 21, "tt": 7}),
 "soya_sosu": I("Soya sosu", "diger", 53, 8, 0.6, 4.9, {"yk": 17}),
 "salca": I("Domates salçası", "diger", 82, 4.3, 0.5, 19, {"yk": 17}),
 "domates_konserve": I("Doğranmış domates (konserve)", "diger", 21, 1, 0.2, 4.3),
 "miso": I("Miso ezmesi", "diger", 199, 12, 6, 26, {"tt": 6}),
 "kakao": I("Kakao (şekersiz)", "diger", 228, 19.6, 13.7, 57.9, {"yk": 6}),
 "susam": I("Susam", "diger", 573, 18, 50, 23, {"tt": 3}),
 "hardal": I("Hardal", "diger", 66, 4, 4, 6, {"tt": 5}),
 "sweet_chili": I("Sweet chili sos", "diger", 200, 0.3, 0, 50, {"yk": 17}),
 "tavuk_suyu": I("Tavuk suyu (tuzsuz)", "diger", 10, 1, 0.2, 0.5),
 "baharat": I("Baharat", "diger", 300, 12, 10, 50, {"tt": 2}),
 "kabartma": I("Kabartma tozu", "diger", 53, 0, 0, 28, {"tt": 4}),
 "su": I("Su", "diger", 0, 0, 0, 0),
 "tuz": I("Tuz, karabiber", "diger", 0, 0, 0, 0),
}

# (key, miktar, birim, not)  -> 3 porsiyonluk miktarlar
R = []
def rec(id, section, kind, title, cuisine, time, portion, ing, steps, family, swap):
    R.append(dict(id=id, section=section, kind=kind, title=title, cuisine=cuisine, time=time,
                  portion=portion, ing=ing, steps=steps, family=family, swap=swap))

# ---------------- KAHVALTI ----------------
rec("B1","kahvalti","","Hindi kıymalı shakshuka","İsrail / Kuzey Afrika","25 dk",
 "Tavanın üçte biri + 1 dilim ekmek",
 [("yumurta",6,"adet",""),("yumurta_aki",4,"adet",""),("hindi_gogus_kiyma",200,"g",""),("domates",450,"g","rendelenmiş"),
  ("kirmizi_biber",150,"g","doğranmış"),("sogan",90,"g","doğranmış"),("sarimsak",3,"diş",""),
  ("zeytinyagi",1,"tt",""),("baharat",2,"tt","kimyon, tatlı kırmızı biber"),("ekmek",3,"dilim",""),("tuz",0,"g","")],
 ["Soğan ve biberi zeytinyağında yumuşat, kıymayı ekleyip kavur, sarımsak ve baharatı ekle.","Domatesi ekleyip 10 dk koyulaşana kadar pişir.","Yumurtaları ve akları sosa kır, kapağı kapat, 6-7 dk pişir.","Ekmekle servis et."],
 "Tek tavada pişer. Pul biber masada, ekmeği herkes kendi alır.","Hindi kıyma yerine az yağlı dana kıyma; akların yerine 2 yumurta.")
rec("B2","kahvalti","","Tamagoyaki, soyalı tavuk, edamame ve miso çorbası","Japonya","25 dk",
 "2 dilim tamagoyaki + tavuk + edamame + çorba + küçük kase pilav",
 [("yumurta",6,"adet",""),("yumurta_aki",4,"adet",""),("tavuk_gogsu",150,"g","ince dilim"),("soya_sosu",2,"yk",""),("bal",1,"tt",""),
  ("miso",3,"tt",""),("su",600,"ml",""),("yesil_sogan",30,"g",""),("edamame",150,"g","haşlanmış"),("pilav",180,"g","")],
 ["Yumurta, akları ve soya sosunun yarısını çırp; yağlı tavada ince katmanlar halinde sararak 3-4 kat yap, dilimle.","Tavuk dilimlerini kalan soya sosu ve balla 4-5 dk tavada pişir.","Misoyu sıcak suda çöz (kaynatma), yeşil soğan ekle.","Edamame ve pilavla servis et."],
 "Pilav, edamame ve tavuk ayrı kasede; herkes payını ayarlar.","Miso bulunamazsa soya sosu + sebze suyuyla hafif çorba.")
rec("B3","kahvalti","","Yumurtalı Meksika wrap'ı","Meksika","15 dk",
 "1 wrap + yanında yoğurt sos",
 [("yumurta",4,"adet",""),("yumurta_aki",3,"adet",""),("tortilla",3,"adet",""),("hindi_fume",200,"g","şerit"),
  ("mozzarella",50,"g","rendelenmiş"),("domates",200,"g","doğranmış"),("yesil_biber",100,"g",""),("sogan",60,"g",""),
  ("suzme_yogurt",200,"g","sos için"),("limon",1,"adet",""),("baharat",1,"tt","kimyon"),("taze_ot",10,"g",""),("tuz",0,"g","")],
 ["Soğan, biber ve domatesi tavada 3-4 dk sotele, hindiyi ekle.","Yumurta ve akları ekleyip karıştırarak pişir.","Tortillaları ısıt, yumurtalı karışımı ve peyniri koyup sar.","Limonlu kimyonlu yoğurtla servis et."],
 "İç harç ortak, wrap'i herkes kendi sarar. Jalapeño veya acı sos masada.","Hindi yerine tavuk füme.")
rec("B4","kahvalti","","Lorlu protein pankek","Amerika","20 dk",
 "4 küçük pankek + meyve",
 [("lor",300,"g",""),("yumurta",3,"adet",""),("whey",2,"ölçek",""),("tb_un",6,"yk","tam buğday unu"),
  ("kabartma",1,"tt",""),("bal",1,"yk",""),("cilek",200,"g",""),("baharat",1,"tt","tarçın")],
 ["Lor, yumurta, whey, un ve kabartma tozunu blenderda pürüzsüz karıştır.","Hafif yağlı tavada küçük pankekleri her yüzü 2 dk pişir.","Çilek, bal ve tarçınla servis et."],
 "Hamur bir kerede hazırlanır; whey sadece senin payına eklemek istersen hamuru ikiye bölebilirsin.","Whey yoksa 1 yumurta ve 60 g lor daha ekle.")

rec("B5","kahvalti","","Kıymalı menemen","Türkiye","15 dk",
 "Tavanın üçte biri + 1 dilim ekmek",
 [("dana_kiyma",300,"g","az yağlı"),("yumurta",5,"adet",""),("yumurta_aki",3,"adet",""),("domates",400,"g",""),
  ("yesil_biber",150,"g","sivri biber"),("sogan",90,"g",""),("zeytinyagi",2,"tt",""),("ekmek",3,"dilim",""),("baharat",1,"tt","pul biber, kekik"),("tuz",0,"g","")],
 ["Kıymayı kuru tavada kavur, kenara al.","Soğan, biber ve domatesi zeytinyağında pişir.","Kıymayı geri ekle, yumurta ve akları kır, hafifçe karıştırarak pişir.","Ekmekle servis et."],
 "Klasik menemen gibi ortak tavadan servis edilir.","Kıyma yerine hindi göğüs kıyma veya didiklenmiş tavuk.")
rec("B6","kahvalti","","Yunan usulü yoğurt bowl","Yunanistan","5 dk",
 "1 büyük kase (~350 g)",
 [("suzme_yogurt",600,"g",""),("whey",2,"ölçek",""),("ceviz",30,"g","kırılmış"),("nar",150,"g",""),("bal",1,"yk",""),("baharat",1,"tt","tarçın")],
 ["Yoğurdu whey ile pürüzsüz karıştır.","Kaselere paylaştır.","Ceviz, nar, bal ve tarçını ekle."],
 "Toppingler ortada durur, herkes kendi kasesini kurar. Whey sadece senin kasene de karıştırılabilir.","Whey olmadan protein ~%25 düşer. Cevizi fındıkla değiştirebilirsin.")

rec("B7","kahvalti","","Besan chilla, lor ve nane yoğurdu","Hindistan","25 dk",
 "2 chilla + yoğurt",
 [("nohut_unu",120,"g",""),("su",200,"ml",""),("yumurta",3,"adet",""),("baharat",2,"tt","zerdeçal, kimyon"),("sogan",60,"g","ince doğranmış"),
  ("domates",100,"g",""),("taze_ot",10,"g",""),("lor",300,"g",""),("suzme_yogurt",300,"g","nane ve sarımsakla"),("tuz",0,"g","")],
 ["Un, su, yumurta ve baharatı karıştır, 10 dk dinlendir. Soğan, domates ve otları ekle.","Yapışmaz tavada ince krepleri iki yüzü de pişir.","İçine lor koy, katla.","Nane-sarımsaklı yoğurtla servis et."],
 "Hamur bir kere hazırlanır, içine herkes istediğini koyar.","Nohut unu bulunamazsa kuru nohutu öğütebilirsin.")

rec("B8","kahvalti","","Gyeran-jjim (buğulama yumurta) ve karides","Kore","20 dk",
 "1 kase jjim + 1 kase pilav",
 [("yumurta",7,"adet",""),("yumurta_aki",4,"adet",""),("su",300,"ml","sıcak"),("soya_sosu",1,"yk",""),("karides",240,"g","soyulmuş"),
  ("yesil_sogan",30,"g",""),("susam_yagi",1,"tt",""),("pilav",180,"g","pişmiş")],
 ["Yumurta ve akları çırp, suyu ve soya sosunu ekle, süz.","Karides ve yeşil soğanı 3 kaseye paylaştır, yumurtayı üstüne dök.","Kısık ateşte buharda 12-15 dk pişir.","Susam yağı damlat, pilavla servis et."],
 "Kaseler aynı anda buharda pişer. Pilav yan tarafta.","Karides yerine didiklenmiş tavuk veya hindi füme.")

rec("B9","kahvalti","","Humus, haşlanmış yumurta ve süzme peynirli lavaş tabağı","Levant","15 dk",
 "Tabak: 1-2 yumurta, peynir, humus, ½ lavaş",
 [("yumurta",5,"adet","haşlanmış"),("suzme_peynir",300,"g",""),("humus",60,"g",""),("lavas",1.5,"adet",""),("hindi_fume",180,"g",""),
  ("salatalik",150,"g",""),("domates",150,"g",""),("taze_ot",10,"g",""),("baharat",1,"tt","zahter veya sumak")],
 ["Yumurtaları 9-10 dk haşla, soğut, soy.","Humusu geniş tabağa yay, zahter gezdir.","Sebzeleri doğra, süzme peynir ve hindi ile diz.","Lavaşı ısıt, ortaya servis et."],
 "Mezze mantığı: ortaya koyulur, herkes alır.","Süzme peynir yerine lor; hindi yerine tavuk füme.")

rec("B10","kahvalti","","Hindi füme ve ıspanaklı frittata","İtalya","10 + 20 dk fırın",
 "2 dilim frittata + yarım lavaş",
 [("yumurta",6,"adet",""),("yumurta_aki",3,"adet",""),("hindi_fume",250,"g","doğranmış"),("kasar",60,"g","rendelenmiş"),
  ("ispanak",200,"g",""),("sogan",90,"g",""),("zeytinyagi",1,"tt",""),("lavas",1.5,"adet","")],
 ["Soğanı ve ıspanağı tavada yumuşat.","Yumurta, akları, hindi ve peynirle karıştır.","Yağlanmış tepsiye dök, 180°C fırında 20 dk pişir.","Dilimle, lavaşla servis et."],
 "Meal prep dostu: 2-3 gün buzdolabında durur, sabah ısıtılır.","Hindi yerine tavuk füme; kaşar yerine mozzarella.")
# ---------------- AKŞAM ----------------
rec("D1","aksam","","Limonlu yoğurtlu tavuk but, fırın patates","Yunanistan","15 + 40 dk fırın",
 "1 tepsi payı: tavuk + patates + tzatziki",
 [("tavuk_but",600,"g","derisiz, kemiksiz"),("patates",600,"g","dilimlenmiş"),("limon",2,"adet",""),("sarimsak",4,"diş",""),
  ("zeytinyagi",1,"yk",""),("baharat",1,"tt","kekik"),("yogurt",200,"g","tzatziki için"),("salatalik",100,"g",""),("domates",200,"g",""),("tuz",0,"g","")],
 ["Tavuğu limon, sarımsak, kekik ve zeytinyağıyla 30 dk (ya da gece boyu) marine et.","Patatesi dilimleyip tepsiye diz, tavuğu üstüne yerleştir.","200°C fırında 40 dk pişir.","Rendelenmiş salatalıklı yoğurtla (tzatziki) ve domatesle servis et."],
 "Tek tepsi. Patates miktarını tabakta herkes ayarlar.","Tavuk but yerine göğüs (daha yağsız, oran iyileşir); kuzu parçaları da olur.")

rec("D2","aksam","","Fırın levrek, otlu sebze, pilav, sarımsaklı yoğurt","Akdeniz / Türkiye","35 dk",
 "1 levrek fileto + sebze + 1 kase pilav",
 [("levrek",700,"g","fileto"),("kabak",300,"g",""),("domates",200,"g","kiraz domates"),("zeytinyagi",1,"yk",""),("limon",2,"adet",""),
  ("sarimsak",3,"diş",""),("taze_ot",20,"g","dereotu, maydanoz"),("pilav",450,"g","pişmiş"),("yogurt",200,"g","sarımsakla"),("tuz",0,"g","")],
 ["Sebzeleri tepsiye ser, üstüne balık filetolarını, limon ve otları koy.","200°C fırında 15-18 dk pişir.","Pilavı ısıt.","Sarımsaklı yoğurtla servis et."],
 "Balık tepsisi ortada, pilav ayrı. Balık sevmeyen için aynı tepsiye tavuk.","Levrek yerine çipura, mezgit veya beyaz bir balık.")

rec("D3","aksam","","Dana bulgogi bowl","Kore","30 dk",
 "1 bowl: et + pilav + sebze",
 [("dana_bonfile",600,"g","ince dilim"),("soya_sosu",4,"yk",""),("bal",1,"yk",""),("susam_yagi",1,"tt",""),("sarimsak",4,"diş",""),
  ("elma",1,"adet","rendelenmiş"),("pilav",360,"g","pişmiş"),("havuc",150,"g",""),("salatalik",150,"g",""),("ispanak",150,"g",""),("susam",1,"tt","")],
 ["Eti sos malzemeleriyle 15 dk marine et.","Havuç ve ıspanağı haşla veya kıvamında sotele, salatalığı doğra.","Eti çok sıcak tavada 3-4 dk kavur.","Pilav, et ve sebzeleri bowl'a diz, susam serp."],
 "Bowl'ı herkes kendi kurar. Acı sos masada.","Dana yerine hindi but dilimleri.")

rec("D4","aksam","","Tavuk fajita (air fryer)","Meksika","30 dk",
 "2 mini tortilla + fajita + sos",
 [("tavuk_gogsu",520,"g","şerit"),("kirmizi_biber",300,"g","şerit"),("sogan",150,"g",""),("baharat",3,"tt","kimyon, paprika, sarımsak tozu"),
  ("limon",1,"adet",""),("zeytinyagi",1,"tt",""),("tortilla",6,"adet","mini"),("suzme_yogurt",200,"g","lime ile sos"),("avokado",60,"g","ezme"),("tuz",0,"g","")],
 ["Tavuk ve sebzeyi baharat, limon ve yağla karıştır.","Air fryer'da 200°C'de 12-14 dk, ortada karıştırarak pişir.","Tortillaları ısıt.","Yoğurt sosu ve avokadoyla servis et."],
 "Fajita tavası ortada: herkes kendi taco'sunu yapar.","Air fryer yoksa fırın 220°C'de tepsi veya geniş tava.")

rec("D5","aksam","","Köfte, közlenmiş sebze, yoğurt","Türkiye","40 dk",
 "4 köfte + sebze + yoğurt + 1 lavaş",
 [("dana_kiyma",540,"g","az yağlı"),("yumurta",1,"adet",""),("sogan",100,"g","rendelenmiş"),("taze_ot",10,"g","maydanoz"),
  ("baharat",2,"tt","kimyon, karabiber"),("patlican",300,"g",""),("yesil_biber",150,"g","sivri biber"),("yogurt",300,"g",""),("lavas",2,"adet",""),("tuz",0,"g","")],
 ["Köfte harcını yoğur, 12 parçaya şekillendir.","Patlıcan ve biberi air fryer veya fırında közle.","Köfteleri 190°C'de 12-14 dk pişir.","Yoğurt ve lavaşla servis et."],
 "Aile yemeği klasiği, kimseye ayrı yemek yapmaya gerek yok.","Dana kıyma yerine hindi göğüs kıyma (daha hafif) veya yarı yarıya kuzu.")

rec("D6","aksam","","Avgolemono çorbası ve Yunan salatası","Yunanistan","45 dk",
 "1 büyük kase çorba + salata + ⅓ lavaş",
 [("tavuk_gogsu",450,"g",""),("pilav",200,"g","pişmiş"),("tavuk_suyu",1000,"ml",""),("yumurta",2,"adet","terbiye için"),("limon",2,"adet",""),
  ("beyaz_peynir",100,"g",""),("domates",250,"g",""),("salatalik",200,"g",""),("zeytin",40,"g",""),("sogan",40,"g",""),
  ("zeytinyagi",1,"yk",""),("lavas",1,"adet","")],
 ["Tavuğu suda haşla, didikle. Pirinci aynı suda ısıt.","Yumurta ve limonu çırp, sıcak çorbadan azar azar ekleyerek terbiye et.","Tavuğu çorbaya geri ekle, kaynatma.","Salatayla servis et."],
 "Çorba + salata sofranın tamamını doyurur. Lavaş yanında.","Beyaz peynir yerine feta.")

rec("D7","aksam","","Karides wok ve pilav","Tayland","25 dk",
 "1 tabak wok + 1 kase pilav",
 [("karides",700,"g","soyulmuş"),("brokoli",250,"g",""),("havuc",150,"g",""),("kirmizi_biber",150,"g",""),("mantar",200,"g",""),
  ("sarimsak",4,"diş",""),("zencefil",10,"g",""),("soya_sosu",3,"yk",""),("bal",1,"yk",""),("limon",1,"adet",""),
  ("susam_yagi",1,"yk",""),("taze_ot",10,"g","fesleğen"),("pilav",450,"g","pişmiş")],
 ["Sosu soya, bal, limon ve susam yağıyla karıştır.","Wok'ta sarımsak ve zencefili kavur, sert sebzeleri 3-4 dk çevir.","Karidesi ekle, 2-3 dk sonra sosu dök.","Fesleğenle pilavın üstüne servis et."],
 "Pul biber ve sriracha masada. Karides sevmeyen için aynı sos, aynı sebzeyle tavuk versiyonu.","Karides yerine tavuk göğsü şeritleri.")

rec("D8","aksam","","Tavuk tikka ve mercimek dal","Hindistan","50 dk",
 "Tikka + 1 kase dal + pilav",
 [("tavuk_gogsu",500,"g","küp"),("yogurt",150,"g","marine için"),("baharat",3,"tt","garam masala, kimyon, zerdeçal, paprika"),("sarimsak",3,"diş",""),
  ("zencefil",10,"g",""),("limon",1,"adet",""),("mercimek",100,"g",""),("sogan",100,"g",""),("domates",200,"g",""),("zeytinyagi",1,"tt",""),
  ("pilav",240,"g","pişmiş"),("salatalik",150,"g","")],
 ["Tavuğu yoğurt ve baharatlarla en az 30 dk marine et.","Mercimeği soğan, domates ve baharatla 20 dk haşla, ezerek dal yap.","Tavukları air fryer'da 200°C'de 12-15 dk pişir.","Pilav, dal ve tikka ile servis et."],
 "Acı yok, sadece aromatik. Acı sosla sonradan.","Garam masala yoksa kimyon + kuru kişniş + karabiber karışımı.")

rec("D9","aksam","","Kuzu kıymalı patlıcan sarma graten","Türkiye / Orta Doğu","60 dk",
 "3-4 sarma",
 [("kuzu_kiyma",400,"g","yağsız"),("patlican",600,"g","uzunlamasına dilim"),("sogan",100,"g",""),("sarimsak",3,"diş",""),("domates",200,"g","rendelenmiş"),
  ("salca",1,"yk",""),("baharat",2,"tt","kimyon, nane"),("yogurt",300,"g","sos için"),("yumurta",2,"adet",""),("tb_un",1,"yk",""),
  ("kasar",90,"g","rendelenmiş"),("zeytinyagi",1,"yk",""),("tuz",0,"g","")],
 ["Patlıcan dilimlerini fırın veya air fryer'da hafif yağla pişir.","Kıymayı soğan, sarımsak, domates, salça ve baharatla kavur.","Harcı patlıcanlara sar, tepsiye diz.","Yoğurt-yumurta-un sosunu dök, kaşar serp, 190°C'de 25 dk pişir."],
 "Hafta sonu yemeği. Önceden hazırlanıp tepsiye dizilir, akşam fırına girer.","Kuzu kıyma yerine dana kıyma.")

rec("D10","aksam","","Arnavut ciğeri (air fryer), fırın patates ve sumaklı soğan","Türkiye","35 dk",
 "1 porsiyon ciğer + patates + yoğurt",
 [("dana_cigeri",600,"g","küçük küp"),("tb_un",2,"yk",""),("zeytinyagi",1,"yk",""),("baharat",2,"tt","pul biber, kırmızı biber"),("patates",400,"g","küçük küp"),
  ("sogan",150,"g","kırmızı soğan, sumakla"),("taze_ot",10,"g","maydanoz"),("yogurt",300,"g",""),("tuz",0,"g","")],
 ["Ciğeri 20 dk sütlü suda beklet, kurula.","Una ve baharata bulayıp air fryer'da 200°C'de 8-10 dk pişir.","Patatesi ayrıca 18-20 dk çevirerek pişir.","Sumaklı soğan ve yoğurtla servis et."],
 "Tatsız bulanlar için patates ve yoğurt dengeyi sağlar.","Ciğer sevmeyenler için aynı baharatla dana kuşbaşı.")

# ---------------- SNACK ----------------
rec("S1","snack","tatlı","Yoğurtlu meyve bark","Modern","10 dk + dondurma",
 "2 parça bark",
 [("suzme_yogurt",300,"g",""),("bal",1,"yk",""),("cilek",150,"g",""),("yaban_mersini",50,"g","")],
 ["Yoğurdu bal ile karıştır, baskı kağıdında tepsiye ince yay.","Meyveleri bastır.","3-4 saat dondur, kır, dondurucudan çıkarıp ye."],
 "Dondurucuda hep hazır durur.","Yoğurt yerine süzme kefir.")
rec("S2","snack","tatlı","Fırında elma tarçın","Avrupa","30 dk",
 "1 elma + 2 yk yoğurt",
 [("elma",3,"adet",""),("bal",2,"tt",""),("ceviz",10,"g",""),("suzme_yogurt",120,"g",""),("baharat",1,"tt","tarçın")],
 ["Elmaların çekirdeğini çıkar, içine bal, tarçın ve ceviz koy.","180°C fırında 25 dk pişir.","Soğuk yoğurtla servis et."],
 "Tepsi doludur, kim isterse alır.","Elma yerine armut.")
rec("S3","snack","tatlı","Çikolatalı lor mousse","Modern","10 dk + dinlenme",
 "1 küçük kase",
 [("lor",250,"g",""),("kakao",3,"yk",""),("whey_cikolata",1,"ölçek",""),("bal",2,"tt","")],
 ["Tüm malzemeyi blenderda pürüzsüz karıştır.","Kaselere paylaştır.","2 saat buzdolabında dinlendir."],
 "Whey ailenin geri kalanına gerek yok: kaseye sonra ekleyebilirsin.","Whey yoksa 1 yk daha kakao ve bal.")
rec("S4","snack","tatlı","Hafif sütlaç","Türkiye","40 dk",
 "1 küçük kase",
 [("sut",400,"ml",""),("su",300,"ml",""),("pirinc_kuru",35,"g",""),("bal",2,"tt",""),("baharat",1,"tt","tarçın")],
 ["Pirinci suyla 15 dk haşla.","Sütü ekle, 20 dk karıştırarak pişir.","Balı ekle, soğuyunca tarçın serp."],
 "Klasik aile tatlısı, şekeri sen azaltırsın, başkası ekler.","Bal yerine hurma şurubu.")
rec("S5","snack","tatlı","Mango lassi popsicle","Hindistan","10 dk + dondurma",
 "1 popsicle",
 [("mango",250,"g",""),("yogurt",250,"g",""),("bal",1,"tt","")],
 ["Blenderda pürüzsüz yap.","Kalıplara dök.","4-6 saat dondur."],
 "Ev dondurması her mevsim olur.","Mango yerine şeftali veya ananas.")
rec("S6","snack","tuzlu","Baharatlı nohut kıtır","Akdeniz","20 dk",
 "1 avuç (~65 g)",
 [("nohut",200,"g","süzülmüş"),("zeytinyagi",1,"tt",""),("baharat",2,"tt","kimyon, paprika, sarımsak tozu"),("tuz",0,"g","")],
 ["Nohutu iyice kurula.","Yağ ve baharatla karıştır.","Air fryer'da 200°C'de 14-16 dk, ara sıra sallayarak pişir."],
 "Kapalı kutuda 2-3 gün çıtır kalır.","Air fryer yoksa fırın 220°C, 25 dk.")
rec("S7","snack","tuzlu","Limonlu edamame","Japonya","10 dk",
 "1 kase (~100 g)",
 [("edamame",300,"g","dondurulmuş, kabuksuz"),("limon",1,"adet",""),("baharat",1,"tt","pul biber"),("tuz",0,"g","")],
 ["Edamameyi tuzlu suda 5 dk haşla.","Süz, limon ve tuzla karıştır.","Pul biber serp."],
 "Film gecesi atıştırmalığı.","Edamame bulunamazsa haşlanmış bezelye veya bakla.")
rec("S8","snack","tuzlu","Labneli salatalık ruloları","Levant","10 dk",
 "5-6 rulo",
 [("salatalik",400,"g","uzun şeritler"),("labne",150,"g",""),("taze_ot",10,"g","dereotu, nane"),("baharat",1,"tt","zahter veya sumak")],
 ["Salatalığı uzun şeritler halinde soy.","Labne, otlar ve zahteri karıştır.","Şeritlere sür, rulo yap."],
 "Misafir geldiğinde de hemen sunulur.","Labne yerine süzme yoğurt.")
rec("S9","snack","tuzlu","Hindi füme labne roll-up","Amerika","5 dk",
 "3 rulo",
 [("hindi_fume",120,"g","8 dilim"),("labne",90,"g",""),("salatalik",100,"g","çubuk"),("hardal",1,"tt","")],
 ["Hindi dilimlerine labne ve hardalı sür.","Salatalık çubuğunu koy.","Rulo yap."],
 "Çabuk biter.","Hindi yerine tavuk füme.")
rec("S10","snack","tuzlu","Kabak cipsi ve nane yoğurdu","Modern","25 dk",
 "1 kase cips + 2 yk dip",
 [("kabak",600,"g","ince dilim"),("zeytinyagi",1,"tt",""),("baharat",1,"tt","sarımsak tozu"),("yogurt",150,"g","nane ve sarımsakla"),("tuz",0,"g","")],
 ["Kabak dilimlerini yağ ve baharatla karıştır.","Air fryer'da 180°C'de 12-15 dk çevirerek pişir.","Nane yoğurdu ile servis et."],
 "Patates cipsinin yerini tutar.","Kabak yerine havuç veya pancar dilimleri.")

# ---------------- RICE PAPER & NORI ----------------
rec("R1","rice-nori","kahvaltı","Rice paper omlet pizzası","Füzyon","15 dk",
 "1-2 pizza dilimi (tavanın üçte biri)",
 [("rice_paper",8,"yaprak",""),("yumurta",5,"adet",""),("yumurta_aki",3,"adet",""),("mozzarella",70,"g","rendelenmiş"),("hindi_fume",250,"g",""),
  ("domates",150,"g","rendelenmiş"),("baharat",1,"tt","kekik, pul biber"),("tuz",0,"g","")],
 ["Rice paper'ı suda geçir, iki kat yağsız tavaya koy.","Çırpılmış yumurta ve akları üstüne dök, kapağı kapat 3-4 dk.","Domates, hindi ve mozzarellayı ekle, 2 dk daha kapat.","Baharatla servis et."],
 "Herkes kendi pizzasını kendi toppingiyle yapar.","Hindi yerine mantar ve ıspanak (protein oranı düşer).")
rec("R2","rice-nori","kahvaltı","Nori onigiri (hindi füme ve yumurta)","Japonya","25 dk",
 "3 onigiri + yoğurt",
 [("sushi_pirinc",270,"g","pişmiş"),("yumurta",4,"adet",""),("yumurta_aki",3,"adet",""),("hindi_fume",200,"g",""),("nori",4,"yaprak",""),
  ("suzme_yogurt",250,"g","yanında"),("soya_sosu",1,"yk",""),("susam",1,"tt","")],
 ["Yumurta ve akları omlet yap, şeritle.","Pirinci ıslak elle üçgenle, ortasına yumurta ve hindi koy.","Nori ile sar, susam serp.","Yoğurt veya soya sosuyla servis et."],
 "Okula veya işe de gider.","Hindi yerine füme somon.")
rec("R3","rice-nori","kahvaltı","Çıtır kahvaltı spring roll (air fryer)","Füzyon","25 dk",
 "3 rulo + yoğurt sos",
 [("rice_paper",9,"yaprak",""),("yumurta",4,"adet",""),("yumurta_aki",3,"adet",""),("hindi_fume",150,"g","doğranmış"),("beyaz_peynir",100,"g",""),("ispanak",200,"g",""),
  ("sarimsak",2,"diş",""),("suzme_yogurt",300,"g","sos için"),("limon",1,"adet","")],
 ["Ispanak ve sarımsağı kuru tavada sotele, yumurta ve akları ekleyip karıştırarak pişir, hindiyi ekle.","Rice paper'ı ıslat, harç ve peyniri koyup sar.","Air fryer'da 180°C'de 8-10 dk çıtırlaştır.","Limonlu, sarımsaklı yoğurtla servis et."],
 "Çıtır dokusu sevenler için.","Beyaz peynir yerine lor.")
rec("R4","rice-nori","kahvaltı","Rice paper lor-whey meyveli börek (tatlı)","Füzyon","15 dk + dinlenme",
 "1 dilim (tepsinin üçte biri)",
 [("rice_paper",9,"yaprak",""),("lor",450,"g",""),("whey",2,"ölçek",""),("cilek",250,"g",""),("bal",1,"yk",""),("baharat",1,"tt","tarçın")],
 ["Lor, whey ve balı karıştırıp krema yap.","Rice paper'ı ıslat, krema ve meyveyle 3 kat diz.","1 saat buzdolabında dinlendir.","Tarçınla servis et."],
 "Tatlı kahvaltı için; whey sadece sana ayrı bir kaseye eklenebilir.","Çilek yerine mevsim meyvesi.")
rec("R5","rice-nori","kahvaltı","Nori somon-labne rulo, yumurta ve süzme peynir","Japonya / İskandinav","15 dk",
 "3-4 rulo + 2 yumurta + peynir",
 [("nori",4,"yaprak",""),("fume_somon",200,"g",""),("labne",150,"g",""),("salatalik",200,"g",""),("yumurta",6,"adet","haşlanmış"),
  ("suzme_peynir",250,"g",""),("limon",1,"adet","")],
 ["Nori üstüne labneyi sür, somon ve salatalığı diz.","Sıkıca sar, dilimle.","Yumurtaları haşla.","Süzme peynir ve limonla servis et."],
 "Brunch sofrası gibi.","Füme somon yerine hindi füme veya ızgara tavuk.")
rec("R6","rice-nori","akşam","Çıtır karides spring roll (air fryer) ve avokado","Vietnam","35 dk",
 "5 spring roll + sos",
 [("rice_paper",15,"yaprak",""),("karides",700,"g","soyulmuş"),("havuc",150,"g",""),("lahana",200,"g",""),("salatalik",100,"g",""),
  ("sarimsak",3,"diş",""),("soya_sosu",1,"yk",""),("bal",1,"yk",""),("limon",2,"adet",""),("zeytinyagi",1,"tt","fırçalamak için"),("avokado",100,"g","")],
 ["Karidesi sarımsak ve soya ile 3 dk sotele.","Rice paper'a sebze ve karides koyup sar.","Hafif yağlayıp air fryer'da 190°C'de 8-10 dk pişir.","Bal-limon-soya sosla ve avokadoyla servis et."],
 "Sarma masası: herkes kendi spring roll'unu sarar.","Karides yerine tavuk göğsü şeritleri.")
rec("R7","rice-nori","akşam","Rice paper mantısı, sarımsaklı yoğurt","Türkiye / Füzyon","50 dk",
 "10-12 mantı + yoğurt",
 [("rice_paper",18,"yaprak","her biri 4 kare"),("hindi_gogus_kiyma",550,"g",""),("sogan",100,"g",""),("baharat",2,"tt","karabiber, pul biber"),
  ("yogurt",450,"g",""),("sarimsak",3,"diş",""),("zeytinyagi",1,"tt","pul biberli yağ için"),("tuz",0,"g","")],
 ["Kıymayı soğan ve baharatla yoğur.","Rice paper'ı ıslatıp karelere böl, harçla doldur, kapat.","Tuzlu kaynar suda 3-4 dk haşla veya air fryer'da çıtır yap.","Sarımsaklı yoğurt ve pul biberli yağla servis et."],
 "Mantı lezzeti, kıvrım derdi yok, hazırlık hızlı.","Hindi kıyma yerine dana kıyma (protein oranı biraz düşer).")
rec("R8","rice-nori","akşam","Somon-karides nori roll ve edamame","Japonya","40 dk",
 "6-8 dilim roll + edamame",
 [("sushi_pirinc",270,"g","pişmiş"),("somon",200,"g","fırınlanmış"),("karides",300,"g","haşlanmış"),("nori",6,"yaprak",""),("salatalik",150,"g",""),
  ("avokado",60,"g",""),("edamame",200,"g","haşlanmış"),("soya_sosu",2,"yk",""),("tuz",0,"g","")],
 ["Pirinci hafif tuzlayıp ılıt.","Noriyi bambu paspasın üstüne koy; pirinç, somon, karides, salatalık ve avokadoyu diz.","Sıkıca sar, dilimle.","Edamame ve soya sosuyla servis et."],
 "Çiğ balık yemeyenler için somon ve karides pişmiş hazırlanır.","Somon yerine ızgara tavuk.")
rec("R9","rice-nori","akşam","Nori taco, baharatlı hindi kıyma","Meksika / Japonya","25 dk",
 "3 nori taco + pilav",
 [("nori",9,"yaprak","kare kesilmiş"),("hindi_gogus_kiyma",480,"g",""),("baharat",3,"tt","kimyon, paprika, sarımsak tozu"),("salca",1,"yk",""),
  ("pilav",360,"g","pişmiş"),("lahana",200,"g",""),("havuc",100,"g",""),("suzme_yogurt",200,"g","lime ile sos"),("limon",1,"adet",""),("avokado",80,"g","")],
 ["Kıymayı baharat ve salçayla kavur.","Pilav, lahana ve havuçla noriye doldur.","Yoğurt-lime sosla servis et."],
 "Taco masası: herkes kendi tabağını hazırlar.","Hindi kıyma yerine dana kıyma.")
rec("R10","rice-nori","akşam","Rice paper lazanya","İtalya / Füzyon","55 dk",
 "1 dilim (tepsinin üçte biri)",
 [("rice_paper",12,"yaprak",""),("hindi_gogus_kiyma",400,"g",""),("domates_konserve",400,"g",""),("salca",1,"yk",""),("sogan",100,"g",""),
  ("sarimsak",3,"diş",""),("lor",300,"g",""),("mozzarella",90,"g","rendelenmiş"),("ispanak",200,"g",""),("zeytinyagi",1,"tt",""),("baharat",1,"tt","kekik, fesleğen")],
 ["Kıymayı soğan ve sarımsakla kavur, domates ve salçayı ekle, 15 dk pişir.","Rice paper'ı ıslat, tepsiye kat kat sos, lor ve ıspanakla diz.","Mozzarella serp, 180°C'de 25 dk pişir.","5 dk dinlendirip dilimle."],
 "Klasik lazanya hissinde ama hamursuz ve çok daha hafif.","Hindi yerine dana kıyma.")
