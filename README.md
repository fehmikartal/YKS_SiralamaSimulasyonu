# YKS Sıralama Simülasyonu
 YKS Sıralama Simülasyonu, son 4 yılın (2019-2022) verilerini alarak yıllar arasındaki sıralamaların artış/azalışlarını hesaplar ve bu artış/azalışlara göre 2023'te gelebilecek sıralamaları tahmin eder.

 - **❗️ En yakın olduğu yıl olması açısından 2022 verileri daha sağlıklıdır. Yüzdesel sonuçlar sayısal sonuçlardan daha sağlıklıdır. "results.txt" dosyasına da 2022 verilerine göre yüzdesel sonuçlar kaydedilir ❗️**
 - Program sadece geçmiş yıllardaki yüzdelik değişimlere göre hesaplama yapar. Kesin sonuçlar vermez.
 - Veri girişi *"(üniversite adı / bölüm / 2022 / 2021 / 2020 / 2019)"* şeklindedir.
 - Örnek veri girişi:
 ```
itü pc 1179 1821 2450 2580
```
Örnek sonuç:
 ```
-----itü pc-----
Yıllara göre sayısal artış // 20: 130 // 21: 629 // 22: 642        
Yıllara göre yüzdelik artış // 20: %5 // 21: %26 // 22: %35        
Sayısal artışa göre 2023 Tahmini // 20: 1049 // 21: 550 // 22: 537 
Yüzdesel artışa göre 2023 Tahmini // 20: 1120 // 21: 876 // 22: 763
```

**29.07.2023** tarihinde yapılan test sonuçları: *(results.txt dosyasında)*
```
boun pc / Yüzdesel: 303 / Sayısal: 303
bilkent pc / Yüzdesel: 284 / Sayısal: 268
odtü pc / Yüzdesel: 736 / Sayısal: 708
itü pc / Yüzdesel: 763 / Sayısal: 537
özyeğin pc / Yüzdesel: 940 / Sayısal: 781
tobb pc / Yüzdesel: 1209 / Sayısal: 1097
yeditepe pc / Yüzdesel: 1713 / Sayısal: 958
galatasaray pc / Yüzdesel: 2253 / Sayısal: 1911
hacettepe pc / Yüzdesel: 2437 / Sayısal: 1904
itü yapayzeka / Yüzdesel: 994 / Sayısal: 511
boun endüstri / Yüzdesel: 1297 / Sayısal: 1279
```
