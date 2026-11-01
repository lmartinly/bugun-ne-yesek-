# -*- coding: utf-8 -*-
"""h_raw.json içindeki 72 tarifin yapılış adımları, ortak sofra ve alternatif notları.
Anahtar: h_raw.json'daki id. title/portion/ing yalnızca değişen tariflerde verilir.
Skyr geçen yerler protein quark olarak yazıldı (skyr de olur)."""

T = {}
def t(i, steps, family, swap, title=None, portion=None, ing=None):
    T[i] = dict(steps=steps, family=family, swap=swap, title=title, portion=portion, ing=ing or {})

# ---------------- KAHVALTI ----------------
t(1, ["Soğanı ve doğranmış biberi zeytinyağında orta ateşte 5 dk, yumuşayana kadar çevir.",
      "Rendelenmiş domatesi ve baharatı ekle; 8-10 dk suyunu çekene kadar pişir.",
      "Lor peynirini ezip sosa karıştır, 2 dk ısıt.",
      "Yumurtaları ve yumurta aklarını hafifçe çırpıp tavaya dök; kısık ateşte yavaşça karıştırarak 3-4 dk, hâlâ nemli kalacak şekilde pişir.",
      "Ocaktan al ve hemen servis et; menemen sıcak tavada pişmeye devam eder."],
  "Tek tavada pişer; ekmek ve pul biber masada durur.", "Lor yerine süzme peynir veya cottage cheese.")
t(2, ["Hindi göğsünü küçük küpler doğra, ince doğranmış soğanla fırına girebilen tavada zeytinyağında 6-7 dk kavur.",
      "Ispanağı ekle, 2 dk soldur ve fazla suyunu buharlaştır.",
      "Yumurta ve akları tuz ve karabiberle çırpıp tavaya dök, üzerine rendelenmiş mozzarellayı serp.",
      "Kapağı kapalı, kısık ateşte 8-10 dk (ya da 180°C fırında 12 dk) pişir; ortası oturunca dilimle."],
  "Ertesi sabah soğuk da yenir, sandviçe de girer.", "Hindi yerine tavuk göğsü; mozzarella yerine light beyaz peynir.")
t(3, ["Mantarları dilimle; geniş tavada zeytinyağıyla yüksek ateşte, suyunu salıp çekene kadar 6-8 dk sotele. Tuzu en sona bırak.",
      "Taze soğanı ekleyip 1 dk daha çevir, tavadan alıp kenara ayır.",
      "Yumurta, akları ve baharatı çırp; yapışmaz tavada iki partide, kısık ateşte 3-4 dk, kenarları tutunana kadar pişir.",
      "Omletin yarısına lor ve mantar harcını yay, ikiye katla.",
      "Porsiyonlara böl ve sıcak servis et."],
  "İki büyük omlet yapıp üçe bölmek yeterli.", "Mantar yerine kabak veya ıspanak.")
t(4, ["Ekmekleri tost makinesinde veya kuru tavada kızart.",
      "Yumurta aklarını tuzla çırpıp yağsız tavada ince bir omlet gibi 2-3 dk pişir, ekmeğe uyacak şekilde kes.",
      "Ekmeklere cottage cheese sür, ak omleti yerleştir.",
      "Füme somonu ve ince dilimlenmiş salatalığı diz, limon suyu ve karabiber gezdir."],
  "Herkes kendi tostunu kurar.", "Cottage cheese yerine lor; füme somon yerine füme hindi.")
t(5, ["Yulafı blenderda toz haline getir; yumurta, yumurta akı, whey ve kabartma tozuyla pürüzsüz bir hamur olana kadar karıştır. 5 dk dinlendir.",
      "Yapışmaz tavayı yağsız ısıt; kepçeyle küçük pankekler dök. Yüzeyde kabarcıklar çıkınca çevirip 1 dk daha pişir.",
      "Çileği dilimle.",
      "Pankekleri quark ve çilekle servis et."],
  "Hamur bir seferde hazırlanır; herkes kendi toppingini seçer.", "Whey yoksa 1 yumurta ve 40 g yulaf ekle. Quark yerine süzme yoğurt.",
  title="Vanilyalı quark pancake")
t(6, ["Yulafı kuru tavada 3-4 dk, kokusu çıkana kadar kavur ve soğut.",
      "Quark, whey, labne ve limon suyunu çırpma teliyle topaksız karıştır; çok koyuysa 1-2 yk su ekle.",
      "Çileklerin yarısını ezip kremaya hafifçe karıştır, kalanını dilimle.",
      "Kaselere krema, çilek ve yulafı katman katman diz; en az 30 dk soğut."],
  "Önceden hazırlanır, soğuk servis edilir.", "Whey yerine 1 yk bal ve biraz daha quark.")
t(7, ["Tavuk göğsünü ince şeritler kes; baharat, limon suyu, tuz ve 2-3 yk yoğurtla 10 dk (zaman varsa daha uzun) marine et.",
      "Geniş tavada yüksek ateşte 6-7 dk, her yanı kızarana kadar çevir.",
      "Tortillaları kuru tavada 20 sn ısıt.",
      "Lavaşa yoğurt sür; marul, domates, salatalık ve tavuğu yerleştirip sıkıca sar, ikiye kes."],
  "Dolgular ayrı kaselerde durur, herkes kendi dürümünü sarar.", "Tavuk yerine hindi göğsü.")
t(8, ["Fırını 180°C'ye ısıt, muffin kalıbını yağla.",
      "Hindiyi küçük doğra, kapya biberle birlikte yağda 5 dk çevir; ıspanağı ekleyip solmasını bekle, suyunu süz.",
      "Yumurta ve akları tuz ve karabiberle çırp; soğuyan harcı ve rendelenmiş mozzarellayı ekle.",
      "Kalıp gözlerinin 3/4'ünü doldur; 18-20 dk, üstü tutup ortası oturana kadar pişir.",
      "Kalıptan çıkarmadan 5 dk dinlendir."],
  "Kapalı kapta ertesi güne saklanır; mikrodalgada 30 sn yeter.", "Hindi yerine tavuk göğsü; ıspanak yerine mantar.")
t(9, ["Mantarı dilimle, karidesi iyice kurula.",
      "Wok veya geniş tavayı yüksek ateşte ısıt; mantarı 3 dk kavur, karidesi ekle ve her yüzü 1-2 dk, pembeleşene kadar çevir.",
      "Yumurta ve akları soya sosu ve susam yağıyla çırp.",
      "Taze soğanı karideslere ekle, yumurtayı dök; kısık ateşte kenarlar tutunana kadar 3-4 dk pişir.",
      "Porsiyonlara böl, taze soğan yeşilliğiyle servis et."],
  "Pilavla da, tek başına da olur; pul biber masada.", "Karides yerine doğranmış tavuk göğsü.")
t(10, ["Patatesi ince dilimle; soğanla birlikte yağlı tavada, kapak altında 12-15 dk yumuşayana kadar pişir.",
       "Yumurta ve akları tuz ve karabiberle çırp; sıcak patatesin üzerine dök, kısık ateşte 6-8 dk pişir.",
       "Büyük bir tabakla çevirip diğer yüzünü 3-4 dk pişir.",
       "Quark'ı tuz ve doğranmış maydanozla karıştır; tortillayla birlikte servis et."],
   "Soğuk da yenir; dilimleyip kutuya konur.", "Quark yerine süzme yoğurt.")
t(11, ["Yumurta, akları, un ve bir tutam tuzu çırp; yaklaşık yarım su bardağı su ekleyip akışkan hamur yap. 10 dk dinlendir.",
       "Hafif yağlı tavada 6 ince krep pişir (her yüz 1 dk).",
       "Ispanağı 2 dk soldur, lor ve tuz-karabiberle karıştır.",
       "Dolguyu krepleri doldurup katla; tavada her yüzü 1 dk ısıt.",
       "Yoğurtla servis et."],
   "Kreplerin dolgusunu herkes kendi seçebilir; tatlısı için çilek de olur.", "Ispanak yerine mantar veya pazı.")
t(12, ["Fırını 200°C'ye ısıt. Domates ve biberi doğrayıp yağ ve baharatla 6-8 dk sotele, fırın kabına al.",
       "Beyaz peyniri ve lor peynirini ezip sebzelerin arasına yay.",
       "Yumurta ve akları hafifçe çırpıp üzerine dök.",
       "12-15 dk, kenarlar kabarıp ortası oturana kadar pişir.",
       "Kabında, ekmekle servis et."],
   "Fırında kendi kendine pişer, sofraya kabıyla gelir.", "Beyaz peynir yerine light feta.")
t(13, ["Ton balığını süzüp çatalla ez; quark, hardal ve doğranmış turşuyla karıştır.",
       "Yumurta aklarını tuzla çırpıp yağsız tavada ince omlet gibi pişir ve ekmeğe uygun kes.",
       "Ekmekleri kızart; üzerine ak omleti ve ton harcını yay.",
       "Salatalık dilimleriyle tamamla."],
   "Ton harcı ortak kasede durur, herkes kendi sandviçini doldurur.", "Ton balığı yerine haşlanmış tavuk.")
t(14, ["Meyvelerin yarısını donmuş kullanırsan kıvam koyulaşır.",
       "Quark, whey, çilek, yaban mersini ve muzu blenderda koyu kıvamda çek; gerekirse 1-2 yk su ekle.",
       "Kaselere paylaştır.",
       "Üzerine kalan meyveleri ve yulafı serp."],
   "Herkes kendi kasesini süsler.", "Whey yoksa biraz daha quark ve 1 yk bal.")
t(15, ["Yumurta, akları, whey, tarçın ve yaklaşık 100 ml suyu pürüzsüz karıştır.",
       "Ekmek dilimlerini karışıma her yüzü 30 sn batır.",
       "Yapışmaz tavada yağsız, orta ateşte her yüzü 2-3 dk altın rengi alana kadar pişir.",
       "Quark ve çilekle servis et."],
   "Çocukluk lezzeti; tarçın masada.", "Whey yoksa 2 yumurta daha ekle ve quark miktarını artır.",
   portion="1 dilim French toast + quark ve çilek")
t(61, ["Quark'ı limon suyu, ince kıyılmış dereotu, tuz ve karabiberle karıştır.",
       "Ekmek dilimlerini kızart.",
       "Quark kremasını ekmeklere bol sür.",
       "Füme somonu ve ince dilimlenmiş salatalığı diz, dereotuyla süsle."],
   "Üç açık sandviç yeter, kalabalıkta kat kat artar.", "Füme somon yerine füme hindi.",
   title="Füme somonlu tost ve quark kreması")
t(62, ["Soğanı ve biberi yağda 5 dk yumuşat, baharatı ekle.",
       "Rendelenmiş domatesi ekleyip 10 dk koyulaştır.",
       "Süzülmüş ton balığını sosa karıştır; yumurtaları kır, akları da çevresine dök.",
       "Kapağı kapat; kısık ateşte 5-6 dk, yumurtalar tutunana dek pişir.",
       "Maydanozla, ekmekle servis et."],
   "Tek tavada pişer; tavada servis edilir.", "Ton balığı yerine hindi füme veya nohut.")
t(63, ["Quark'ı ezilmiş sarımsak ve tuzla karıştırıp tabaklara yay.",
       "Hindiyi ince dilimle, baharatla yağsız tavada her yüzü 3-4 dk kızart.",
       "Kaynar suda yumurtaları poşe yap (3 dk) veya rafadan pişir.",
       "Yoğurdun üzerine hindi, yumurta ve doğranmış salatalık ile maydanozu yerleştir; zeytinyağı ve baharat gezdir."],
   "Türk kahvaltısının yüksek proteinli hali.", "Hindi yerine tavuk göğsü.",
   title="Çılbır, hindi dilimleri ve yeşillik")
t(64, ["Yulafı blenderda un kıvamına getir.",
       "Lor, yumurta, yulaf, whey, vanilya ve kabartma tozunu pürüzsüz karıştır.",
       "Isıtılıp hafif yağlanmış waffle makinesine kepçeyle dök; 4-5 dk altın rengi olana kadar pişir (makine yoksa küçük pankek yap).",
       "Çilekle servis et."],
   "Hamuru önceden hazırlayıp hafta sonu için bekletebilirsin.", "Whey yoksa 1 yumurta daha ve 1 yk bal.")

# ---------------- AKŞAM ----------------
t(16, ["Tavuğu 3 cm küpler doğra; limon suyu, yağın yarısı, baharat ve tuzla en az 30 dk marine et.",
       "Patatesi dilimleyip kalan yağ ve baharatla 200°C fırında 30-35 dk, ara sıra çevirerek pişir.",
       "Tavukları şişlere diz; fırında veya ızgara tavada her yanını 10-12 dk pişir. Biber ve soğanı yanında közle.",
       "Rendelenmiş salatalığı yoğurt ve tuzla karıştırıp cacığı hazırla.",
       "Tavuk, patates, köz biber ve cacıkla servis et."],
   "Şişler tek tepside pişer, cacık masada kaselerle.", "Tavuk yerine hindi göğsü.")
t(17, ["Çekilmiş hindiyi rendelenmiş soğan, yumurta akı, sarımsağın yarısı, baharat ve tuzla yoğur.",
       "Fırını 200°C'ye ısıt; köfteleri şekillendirip yağlı kâğıtlı tepside 18-20 dk, bir kez çevirerek pişir.",
       "Kabakları yarım ay doğra; zeytinyağında yüksek ateşte 6-8 dk, kenarları kızarana kadar sotele.",
       "Yoğurdu kalan ezilmiş sarımsak ve tuzla karıştır.",
       "Köfte ve kabakları yoğurtla servis et."],
   "Çocukluğumuzun köftesi gibi; yanına bulgur da konabilir.", "Hindi yerine tavuk göğsü kıyma.")
t(18, ["Kıymayı rendelenmiş soğan, 2 diş ezilmiş sarımsak, baharat ve tuzla yoğur; 20 dk dinlendir. Parmak şeklinde koftalar yap.",
       "Patlıcanları çatalla deş, 220°C fırında 25-30 dk yumuşayana kadar közle. Soy, doğra, tuzla.",
       "Koftaları aynı fırında 12-15 dk, bir kez çevirerek pişir.",
       "Yoğurdu kalan sarımsakla karıştır, domatesi doğra.",
       "Patlıcanı yoğurtla katla, koftalar ve domatesle servis et."],
   "Dışarıdan sipariş gibi görünen ama hafif bir sofra.", "Dana kıyma yerine hindi kıyma.")
t(19, ["Tavuğu küp doğra; yoğurdun yarısı ve baharatın yarısıyla 30 dk (varsa gece boyu) marine et. Pirinci 2 kat suyla 12 dk haşla.",
       "Geniş tavada yağda ince doğranmış soğanı 6-7 dk pembeleştir; sarımsak ve kalan baharatı ekleyip 1 dk çevir.",
       "Passatayı ekle ve 8 dk kaynat.",
       "Marine tavuğu ekleyip kapak altında 12-15 dk pişir.",
       "Ocak kapalıyken kalan yoğurdu karıştır (kesilmez); pilavla servis et."],
   "Büyük tencerede pişer, ertesi gün daha lezzetli olur.", "Tavuk yerine hindi; acı için pul biber masada.")
t(20, ["Tavuğu ince şeritler kes; ezilmiş sarımsak ve baharatla 10 dk beklet. Pirinci haşla.",
       "Wok'u çok kızdır, yağı ekle; tavuğu 4-5 dk kızarana kadar karıştırarak pişir, kenara al.",
       "Soğan ve biberi 3-4 dk, çıtır kalacak şekilde çevir.",
       "Tavuğu geri ekle, soya sosunu dök, 1 dk çevir; ateşi kapatıp fesleğeni ekle.",
       "Pilavla servis et."],
   "Acı ayrı: pul biber veya sriracha masada.", "Fesleğen yoksa maydanoz ve biraz daha limon.")
t(21, ["Bonfileyi 3-4 mm ince dilimle (hafif dondurulmuşsa kolay kesilir); soya sosu, bal, ezilmiş sarımsak ve susam yağıyla en az 30 dk marine et. Pirinci haşla.",
       "Havucu çubuk, soğanı ve mantarı dilim doğra.",
       "Wokta sebzeleri yüksek ateşte 4 dk çevir, kenara al.",
       "Eti iki partide 2-3 dk yüksek ateşte kızart; sebzeleri geri ekle.",
       "Pilavla servis et."],
   "Marine önceden hazırlanır, akşam 10 dakikada biter.", "Dana yerine tavuk göğsü.")
t(22, ["Soya sosu, bal, ezilmiş sarımsak, limon suyu ve susam yağını karıştır; balık filetolarını 15 dk bu sosta beklet. Pirinci haşla.",
       "Fırını 200°C'ye ısıt; balıkları tepsiye dizip 10-12 dk pişir.",
       "Brokolileri çiçeklerine ayırıp 4-5 dk buharda veya kaynar suda, yeşil kalacak şekilde haşla.",
       "Kalan marine sosu küçük tencerede 3 dk kaynatıp kıvamlandır, balığa gezdir.",
       "Pilav ve brokoliyle servis et."],
   "Hafif ve hızlı; balığı sevmeyenler için tavuk versiyonu da olur.", "Beyaz balık yerine somon veya tavuk göğsü.")
t(23, ["Pirinci haşlayıp soğut. Lahanayı ince doğra, havucu rendele, salatalığı dilimle.",
       "Lime suyu, soya sosu ve susam yağını karıştırarak sosu hazırla.",
       "Karidesi ezilmiş sarımsakla yüksek ateşte 2-3 dk, her yüzü pembeleşene kadar kavur.",
       "Kaselere pilav, sebzeler ve karidesi paylaştır; sosu gezdir, kişnişle bitir."],
   "Kaseyi herkes kendi kurar.", "Karides yerine tavuk göğsü şeritleri.")
t(24, ["Tavuğu yarım halka soğanla tencerede suda 15-18 dk haşla, süz ve çatalla didikle.",
       "Soğanın kalanını yağsız tavada kavur; passata ve baharatı ekleyip 8 dk kaynat.",
       "Didiklenmiş tavuğu sosa karıştır, 5 dk daha pişir.",
       "Tortillaları kuru tavada ısıt.",
       "Tavuğu tortillalara paylaştır; marul, yoğurt ve lime suyuyla servis et."],
   "Taco bar: herkes kendi sebzesini seçer.", "Tavuk yerine hindi göğsü.")
t(25, ["Çekilmiş tavuk göğsünü tuz ve baharatla yoğurup 3 köfte şekillendir.",
       "Fırını 210°C'ye ısıt; köfteleri yağlı tepside 14-16 dk pişir, acı sosla fırçalayıp 2 dk daha fırınla.",
       "Yoğurdu doğranmış turşuyla karıştırıp sos yap.",
       "Ekmekleri ısıt; sos, marul, domates ve burger köftesiyle kur."],
   "Acı seviyesini herkes kendi ayarlar; sos ayrı kapta.", "Tavuk yerine hindi.",
   ing={"bread": ("Burger ekmeği", 3, "adet")})
t(26, ["Patlıcanı 1 cm halkalar kes, tuzla 10 dk beklet, kurula; yağla fırçalayıp 220°C'de 15 dk pişir.",
       "Tavuk göğsünü yatay ince açıp baharatla tavada her yüzü 3 dk mühürle.",
       "Passatayı fesleğenle 8 dk kaynatıp sos yap.",
       "Fırın kabına patlıcan, tavuk, sos ve mozzarellayı katla; 200°C'de 15-18 dk gratine et."],
   "Dışarıdaki gibi ama kızartma yok.", "Tavuk yerine hindi göğsü.")
t(27, ["Sebzeleri 2 cm küp doğra; yağ ve baharatla karıştırıp tepsiye yay, 200°C'de 25 dk pişir. Domatesi son 15 dk'da ekle.",
       "Hindiyi (çekilmiş) rendelenmiş soğan, tuz ve baharatla yoğurup küçük köfteler yap.",
       "Köfteleri sebzelerin üzerine yerleştirip 15-18 dk daha pişir.",
       "Tepsiyi 5 dk dinlendirip servis et."],
   "Tek tepsi, bulaşık yok.", "Hindi yerine tavuk göğsü kıyma.")
t(28, ["Kıymayı rendelenmiş soğan, yıkanmış pirinç, baharat, tuz ve yağla yoğur.",
       "Biberlerin kapaklarını kes, çekirdeklerini çıkar; harcı yarısına kadar doldur, kapaklarını kapat.",
       "Dar bir tencereye diz; passatayı yarım bardak suyla karıştırıp biberlerin dibine dök.",
       "Kısık ateşte kapağı kapalı 40-45 dk pişir (ya da 180°C fırında).",
       "Yoğurtla servis et."],
   "Annenin dolması gibi, sadece pirinç az ve et fazla.", "Dana yerine hindi kıyma.")
t(29, ["Tavuğu küçük küp doğrayıp baharatla yağsız tavada 8-10 dk pişir; ıspanağı ekle, solunca suyunu süz.",
       "Loru karıştır, tuzla; soğut.",
       "Yufkayı üçgen şeritler kes; harçtan koyup üçgen katla.",
       "Börekleri yağlı kâğıtlı tepsiye diz, yumurta akını sür; 190°C'de 20-25 dk altın rengi olana kadar pişir.",
       "Yoğurtla servis et."],
   "Yağda kızartılmaz; fırın böreği, tüm aile yer.", "Tavuk yerine hindi.")
t(30, ["Kişniş, maydanoz, sarımsak, limon suyu, yağ ve baharatı mutfak robotunda karıştırıp chermoula sosu yap.",
       "Balığı sosun yarısıyla 20 dk marine et.",
       "Patatesi dilimleyip kalan sosla karıştır, 200°C'de 20 dk pişir; domatesi ekle.",
       "Balıkları patateslerin üzerine koy, 10-12 dk daha pişir.",
       "Yoğurtla servis et."],
   "Tek tepsi; sosu bir gün önceden yap.", "Beyaz balık yerine somon veya tavuk.")
t(31, ["Patatesi küp doğra; yağın yarısı, baharat ve tuzla 210°C fırında 30 dk, ara sıra çevirerek kızart. Son 15 dk'da dilimlenmiş biberi ekle.",
       "Karidesi kurula; ince dilimlenmiş sarımsak ve kalan yağla geniş tavada 2-3 dk, pembeleşene kadar kavur.",
       "Yoğurdu limon suyu ile karıştırıp sos yap.",
       "Patates, biber ve karidesi yoğurtla servis et."],
   "Mezelik gibi paylaşarak yenir.", "Karides yerine tavuk.")
t(32, ["Patatesi 15-18 dk haşla, çeyrek böl.",
       "Somonu baharat, tuz ve yağla 200°C'de 12-14 dk pişir.",
       "Quark, limon suyu ve ince kıyılmış dereotunu karıştır.",
       "Marul ve salatalığı doğra; tabaklara patates, salata ve somonu paylaştır, quark sosunu gezdir."],
   "Hafta içi 30 dakikalık şık yemek.", "Somon yerine alabalık.",
   title="Somon, dereotlu quark ve salata")
t(33, ["Dana etini ince şeritler kes; baharat, limon suyu ve birkaç yk yoğurtla 30 dk marine et.",
       "Soğan ve biberi iri doğra; yüksek ateşte yağda 5 dk kavur, kenara al.",
       "Eti iki partide 2-3 dk yüksek ateşte kızart, sebzeleri ekle.",
       "Kalan yoğurdu tuz ve limonla sos yap.",
       "Tabağa marul, domates, sıcak sebze ve eti koy; yoğurt sosla servis et."],
   "Dürüm yapmak isteyen lavaşla da sarar.", "Dana yerine tavuk veya hindi.")
t(34, ["Kuzu kıymayı rendelenmiş soğanın yarısı, yumurta akı, baharat ve tuzla yoğur; 30 dk dinlendir. Şişlere kebap şeklinde sar.",
       "Patlıcan ve biberi 220°C fırında 25 dk köz gibi pişir, soyup doğra.",
       "Kebapları 220°C'de 12-14 dk veya ızgara tavada pişir.",
       "Yoğurt, lor, kalan soğan (ince kıyılmış) ve limon suyundan sos hazırla.",
       "Sebzeler, kebap ve sosla servis et."],
   "Hafta sonu sofrası; mangal yerine fırında olur.", "Kuzu yerine dana kıyma.")
t(35, ["Yoğurt, limon suyu ve baharatla marine karışımı yap; tavukla en az 1 saat (ideal gece boyu) beklet. Servis için 3-4 yk yoğurt ayır.",
       "Karnabaharı çiçeklerine ayır, yağ ve biraz baharatla karıştır, 220°C'de 25 dk pişir.",
       "Tavukları fırın ızgarasında 200°C'de 20-25 dk pişir (iç ısı 74°C).",
       "Soğan halkaları ve ayrılan yoğurtla servis et."],
   "Marinasyon gece yapılırsa akşam sadece fırın.", "Karnabahar yerine brokoli.")
t(36, ["Tavuğu şeritler kes. Pirinci haşla.",
       "Wokta tavuğu yüksek ateşte 4-5 dk mühürleyip al.",
       "Havuç, mantar ve brokoliyi 5-6 dk çıtır kalacak şekilde çevir.",
       "Soya sosu, ezilmiş sarımsak ve susam yağını ekle, tavuğu geri koy, 1-2 dk karıştır.",
       "Pilavla servis et."],
   "Hızlı akşam yemeği; sebze çeşidi serbest.", "Tavuk yerine hindi.")
t(37, ["Çekilmiş hindiyi yumurta akı, baharat ve tuzla yoğurup köfte yap.",
       "200°C fırında 15-18 dk pişir. Pirinci haşla.",
       "Gochujang ve soya sosunu 2-3 yk su ile tavada ısıt, köfteleri 2 dk sosa bulayın.",
       "Lahana ve salatalığı ince doğrayıp quark ile karıştır.",
       "Pilav, salata ve köftelerle servis et."],
   "Gochujang acıysa ayrı sosta bırak.", "Gochujang yerine biberli salça + biraz bal.")
t(38, ["Limon suyu, ezilmiş sarımsak, yağ ve baharatla marine yap; tavuklarla 1 saat beklet.",
       "Patatesi dilimleyip kalan marine ile karıştır, tepsiye yay, 200°C'de 20 dk pişir.",
       "Tavukları patatesin yanına koy; 25-30 dk daha pişir (iç ısı 74°C).",
       "Yoğurdu bir tutam tuz ve baharatla yeşil sos olarak karıştır.",
       "Marul yatağında servis et."],
   "Tek tepsi, kokusuyla herkes sofraya gelir.", "Tavuk yerine hindi göğsü.")
t(39, ["Patlıcanları şeritler halinde soyup yağla fırçala, 220°C'de 15-20 dk pişir.",
       "Soğan ve sarımsağı yağda soteleyip kıymayı ekle; 8 dk kavur, passata ve baharat ekleyip 10 dk pişir.",
       "Patlıcanları kabın dibine diz, kıymayı üzerine yay, 180°C'de 25 dk pişir.",
       "Yoğurtla servis et."],
   "Bilindik bir tat; babana da tanıdık gelir.", "Dana yerine hindi kıyma.")
t(40, ["Misoyu 1 yk su ve yarım soya sosuyla ez; somonlara sür, 15 dk beklet.",
       "200°C fırında somonu 10-12 dk pişir.",
       "Edamame'yi 4-5 dk haşla.",
       "Lahana ve salatalığı ince doğra; quark, lime suyu ve kalan soya sosuyla sos yap.",
       "Kaselere sebze, edamame ve somonu paylaştır; sosu gezdir."],
   "Kase mantığı: herkes sebzesini kendi seçer.", "Somon yerine alabalık.")
t(65, ["Patatesleri küp kes, baharatla 210°C fırında 30 dk kızart.",
       "Kalamarı halkalara kes, kurula. Biberleri doğrayıp yağda 4 dk sotele, çıkar.",
       "Aynı tavayı çok kızdır; kalamarı sarımsakla 2 dk hızlıca pişir (uzarsa lastikleşir), limon suyunu en sona ekle.",
       "Yoğurdu maydanoz ve tuzla karıştır.",
       "Patates, biber, kalamar ve yoğurtla servis et."],
   "Tavada 2 dakika sürer, süre ayarı önemli.", "Kalamar yerine karides.")
t(66, ["Ciğeri 1 cm şeritler kes, soğuk suda 10 dk beklet ve kurula (keskin kokuyu azaltır).",
       "Soğan ve biberi yağda 5 dk yumuşat, kenara al.",
       "Ciğeri baharatla yüksek ateşte 2-3 dk çevir (fazla pişirme).",
       "Domates, lime suyu ve tuzla taze salsa yap.",
       "Tortillalara paylaştır, yoğurt ve salsayla servis et."],
   "Ciğeri sevmeyen için tavuk şeritli versiyon da yapılabilir.", "Ciğer yerine dana bonfile.")
t(67, ["Kabakları boyuna ikiye böl, ortasını kaşıkla oy; oyuntuları ince doğra. Kabakları 3 dk haşla.",
       "Soğanı yağda sotele; kabak oyuntusu, ton balığı, passatanın yarısı ve haşlanmış pirinci ekle, 5 dk pişir.",
       "Kabak yarımlarını doldur, kalan passatayı tepsinin dibine dök.",
       "Mozzarella serp, 190°C'de 25 dk pişir; fesleğenle servis et."],
   "Dolma sevenler için hafif versiyon.", "Ton balığı yerine tavuk göğsü.")
t(68, ["Tavuğu küp doğra; ince kıyılmış soğan, limon suyu, baharat ve yağla 1 saat marine et.",
       "Şişlere diz; ızgara tavada veya 220°C fırında 12-14 dk pişir.",
       "Patatesleri dilimleyip air fryer'da 200°C'de 18-20 dk kızart.",
       "Elmayı rendele, kişniş ve quark ile karıştırıp sos yap.",
       "Şişler, patates ve sosla servis et."],
   "Elmalı sos çocukları bile sevdirir.", "Kişniş yerine maydanoz.")
t(69, ["Soğan ve biberi yağda 5 dk yumuşat; tavuğu, baharatı ve 1,5 L suyu ekle.",
       "Kaynayınca 20 dk pişir, tavukları çıkarıp didikle.",
       "Nohut ve salsayı çorbaya ekle, 10 dk kaynat.",
       "Lahanayı ekle, 5 dk daha pişir; tavuğu geri koy.",
       "Kişniş ve lime suyuyla servis et."],
   "Tek tencere çorba yemeği; ertesi gün kıvam koyulaşır.", "Salsa yoksa domates püresi + pul biber.")
t(70, ["Pirinci haşla ve soğut.",
       "Süzülmüş sardalyayı çatalla ez; quark, doğranmış taze soğan ve soya sosuyla karıştır.",
       "Nori yaprağına ince pirinç tabakası yay; ortaya sardalya harcı ve salatalık çubuklarını koy, sıkıca sar.",
       "Susam serp; kimchiyle servis et."],
   "Kimchi ayrı kasede, sevmeyen almaz.", "Sardalya yerine ton balığı.")
t(71, ["Soğan ve sarımsağı yağda 4 dk kavur; biberi ekle, 3 dk daha pişir.",
       "Passata ve nohudu ekle, 10 dk kaynat.",
       "Balık parçalarını sosun içine yerleştir, kapağı kapat, 8-10 dk pişir.",
       "Maydanoz ve quark ile servis et."],
   "Tencerede servis edilir.", "Balık yerine tavuk göğsü.")
t(72, ["Soğan ve sarımsağı yağda 5 dk kavur, baharatı ekle.",
       "Tavuk küplerini ekleyip 5 dk mühürle, rendelenmiş domatesi ekle; kapak altında 15 dk pişir.",
       "Haşlanmış mercimeği ekle, 5 dk kaynat.",
       "Yoğurtla servis et."],
   "Baharat dozunu hafif tut, acıyı ayrı ver.", "Mercimek yerine nohut.")

# ---------------- RICE PAPER / NORI ----------------
t(41, ["Hindiyi küçük küp doğra, kuru tavada 6-7 dk pişir.",
       "Yumurta ve akları tuz ve karabiberle çırp.",
       "Rice paper'ı kısaca ıslat, iki kat olarak yapışmaz tavaya yay; çırpılmış yumurtayı dök, kısık ateşte 2 dk pişir.",
       "Üstüne hindi, domates, mozzarella ve taze soğanı koy; kapak altında 3 dk, peynir eriyene kadar tut.",
       "Dilimleyip servis et."],
   "Pizza gecesi hafif hali.", "Hindi yerine tavuk veya ton balığı.")
t(42, ["Hindiyi küçük doğra, baharatla yağlı tavada pişir; ıspanağı ekle, solunca suyunu süz.",
       "Lor ve yumurta akını karıştırıp harca ekle.",
       "Rice paper'ı 10 sn ılık suda yumuşat; ortasına harçtan koyup bohça gibi topla.",
       "Air fryer'da 180°C'de 8-10 dk veya yağsız tavada her yüzü 3 dk çıtırlaşana kadar pişir."],
   "Çıtır börek yerine geçer.", "Hindi yerine tavuk.")
t(43, ["Yumurta aklarını tuzla çırpıp yağsız tavada ince omlet pişir, şeritler kes.",
       "Karidesi 2-3 dk her yüzü pembeleşene kadar pişir.",
       "Salatalık ve havucu ince çubuk doğra.",
       "Rice paper'ı ıslat; omlet, karides ve sebzeyi koyup sıkıca sar.",
       "Yoğurt ve soya sosundan dip sos hazırla."],
   "Rulolar önceden sarılıp nemli bezle saklanabilir.", "Karides yerine tavuk.")
t(44, ["Yumurta ve akları çırpıp yağsız tavada ince omlet pişir, şeritler kes.",
       "Süzülmüş ton balığını quark ve ince doğranmış taze soğanla karıştır.",
       "Nori yaprağını ikiye böl; omlet, ton harcı ve salatalık çubuğunu bir köşeye koy.",
       "Koni şeklinde rulla ve hemen servis et (nori nemden yumuşar)."],
   "Herkes kendi rulosunu sarar.", "Ton balığı yerine füme somon.")
t(45, ["Yumurta ve akları çırp, geniş tavada ince bir omlet pişir.",
       "Ispanağı 1-2 dk sotele, suyunu sık, lor ile karıştır.",
       "Omleti tezgâha al, üzerine nori yaprakları yerleştir; lor-ıspanak harcı ve füme somonu yay.",
       "Sıkıca sar, 3 eşit parçaya kes; soya sosuyla servis et."],
   "Sabah acele edenlere yol arkadaşı.", "Füme somon yerine füme hindi.")
t(46, ["Çekilmiş tavuğu çok ince doğranmış lahana, havuç, taze soğan, sarımsak ve soya sosuyla yoğur.",
       "Rice paper'ı ikiye kes, yumuşat; bir yarısına harçtan koyup kapat, kenarlarını bastır.",
       "Yapışmaz tavada az susam yağıyla altlarını 2-3 dk kızart; 3-4 yk su ekle ve kapak altında 4-5 dk buharda pişir.",
       "Soya sosuyla servis et."],
   "Çocuklar da sarmaya katılır.", "Tavuk yerine hindi.")
t(47, ["Hindiyi baharatla yağda 8-10 dk pişir, ıspanağı ekle, suyunu çek.",
       "Lor ve yumurta aklarının yarısı ile karıştır.",
       "Rice paper'ı yumuşat; harçla iki kat yaprakla rulo sar.",
       "Kalan aklarla fırçalayıp air fryer'da 190°C'de 10-12 dk, çevirerek çıtırlaştır."],
   "Börek sevenler için hafif versiyon.", "Hindi yerine tavuk.")
t(48, ["Pirinci haşla, soğut; hafif tuzla.",
       "Ton balığını süzüp quark ve soya sosunun yarısıyla karıştır.",
       "Salatalık ve havucu ince doğra; noriyi makasla şeritler kes.",
       "Kaselere pilav, ton, sebze ve nori koy; kalan soya sosu ve susamla bitir."],
   "Poke bowl mantığı; herkes üstünü seçer.", "Ton balığı yerine somon.")
t(49, ["Pirinci haşla ve fırın kabına yay.",
       "Karidesi doğra; quark, sriracha ve soya sosuyla karıştır, pirincin üzerine yay.",
       "Mozzarella serp; 200°C'de 15-18 dk, üstü tutana kadar pişir.",
       "Nori yaprakları ve salatalıkla sararak ye."],
   "Fırından çıkınca herkes kendi noriyi doldurur.", "Karides yerine tavuk.")
t(50, ["Pirinci haşla ve ıslak elle hafifçe ez.",
       "Tavuğu şeritler kes, soya sosuyla 6-7 dk pişir; akları ince omlet olarak pişir.",
       "Nori yaprağını köşeler size bakacak şekilde koy; ortasına pirinç, marul, omlet, tavuk ve havuç yerleştir, yoğurt sür.",
       "Dört köşeyi ortaya doğru katla, bir dk beklet; keskin bıçakla ikiye kes."],
   "Evde sandviç gibi taşınabilir.", "Tavuk yerine hindi.")

# ---------------- SNACK ----------------
t(51, ["Quark'ı kakao ve stevia ile kremsi olana kadar çırp.",
       "Kaselere paylaştır, çilek dilimlerini ekle.",
       "En az 30 dk buzdolabında soğut."],
   "Kakao azsa biraz daha ekle.", "Stevia yerine 1 tt bal (kalori biraz artar).",
   title="Kakaolu quark mousse")
t(52, ["Elmaları çekirdeklerinden ayırıp 1 cm dilimle; tarçın ve stevia ile karıştır.",
       "Air fryer'da 180°C'de 10-12 dk, ortasında bir kez karıştırarak pişir.",
       "Yoğurtla ılık servis et."],
   "Akşam yemeğinden sonra tatlı niyetine.", "Air fryer yoksa 190°C fırında 15 dk.")
t(53, ["Çileği ezip yoğurtla karıştır.",
       "Silikon mini kalıplara veya parşömen kâğıdına kaşıkla dök.",
       "Üzerine rendelenmiş çikolata serp; 2-3 saat dondur."],
   "Dondurucuda hazır dursun, canın çektiğinde bir avuç al.", "Çilek yerine yaban mersini.")
t(54, ["Muzu halkalara kes, çubuğa veya kürdana tak.",
       "Çikolatayı benmaride erit, kakao ile karıştır.",
       "Muzları bulayıp parşömen kâğıdına koy; 1-2 saat dondur."],
   "Küçük porsiyon, tatlı krizine ilaç.", "Çikolata yerine tarçınlı yoğurt.")
t(55, ["Jelatini 4 yk soğuk suda 5 dk kabart.",
       "Yaban mersinini limon suyuyla hafifçe ez ve ocakta 3 dk ısıt; jelatini ekleyip çöz. Stevia ile tatlandır.",
       "Bardaklara paylaştır, 3-4 saat soğut.",
       "Quark ile servis et."],
   "Önceki akşamdan hazırlanır.", "Yaban mersini yerine çilek.")
t(56, ["Yoğurdu ezilmiş sarımsak, limon, baharat ve tuzla çırp.",
       "Salatalığı çubuk doğra.",
       "Soğuk servis et."],
   "Akşam yemeğinin yanına meze olur.", "Salatalık yerine havuç çubukları.")
t(57, ["Kabağı mandolin veya soyacakla çok ince dilimle, kâğıt havluyla kurula.",
       "Yağ ve baharatla karıştır.",
       "Air fryer'da 160°C'de 12-15 dk, ara sıra karıştırarak çıtır olana kadar pişir; quark ile servis et."],
   "Cipsin yerini tutar.", "Air fryer yoksa 150°C fırında 25 dk.",
   title="Airfryer kabak cipsi")
t(58, ["Edamame'yi 4-5 dk haşla, süz.",
       "Soya sosu, limon suyu ve baharatla harmanla.",
       "Ilık veya soğuk servis et."],
   "TV karşısında kabukla yenir.", "Baharat yerine pul biber.")
t(59, ["Fırını 150°C'ye ısıt.",
       "Nori yapraklarını susam yağıyla hafifçe fırçala, susam ve baharat serp.",
       "Yaprakları kareler kes, 6-8 dk gevrek olana kadar fırınla.",
       "Üç eşit porsiyona böl."],
   "Çabucak bitiyor, çifte yap.", "Susam yağı yerine zeytinyağı.")
t(60, ["Haşlanmış nohudu iyice kurula.",
       "Yağ ve baharatla karıştır.",
       "200°C fırında 20-25 dk, ara sıra karıştırarak gevrek olana kadar pişir; limon suyuyla servis et."],
   "Soğumadan yenir; kapalı kapta ertesi güne yumuşar.", "Baharat yerine kimyon ve pul biber.")
