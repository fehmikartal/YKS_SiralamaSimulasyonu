# Yüzdesel sonuçlar daha doğru olabilir.

info = input("Üniversite Adı / Bölüm Adı / 2022 / 2021 / 2020 / 2019: ")
info = info.split()
name = info[0] + " " +  info[1]
siralama_2022 =  int(info[2])
siralama_2021 =  int(info[3])
siralama_2020 =  int(info[4])
siralama_2019 =  int(info[5])
sayisal_farklar = []
yuzdelik_farklar = []

def sayisal_artis(eski_yil, yeni_yil):
    result = eski_yil-yeni_yil
    sayisal_farklar.append(result)

def yuzdelik_artis(eski_yil, yeni_yil):
    result = (eski_yil-yeni_yil)/eski_yil*100
    yuzdelik_farklar.append(result)

sayisal_artis(siralama_2019, siralama_2020)
sayisal_artis(siralama_2020, siralama_2021)
sayisal_artis(siralama_2021, siralama_2022)

yuzdelik_artis(siralama_2019, siralama_2020)
yuzdelik_artis(siralama_2020, siralama_2021)
yuzdelik_artis(siralama_2021, siralama_2022)

print(f"-----{name}-----")
print(f"Yıllara göre sayısal artış // 20: {sayisal_farklar[0]} // 21: {sayisal_farklar[1]} // 22: {sayisal_farklar[2]}")
print(f"Yıllara göre yüzdelik artış // 20: %{round(yuzdelik_farklar[0])} // 21: %{round(yuzdelik_farklar[1])} // 22: %{round(yuzdelik_farklar[2])}")
print(f"Sayısal artışa göre 2023 Tahmini // 20: {siralama_2022-sayisal_farklar[0]} // 21: {siralama_2022-sayisal_farklar[1]} // 22: {siralama_2022-sayisal_farklar[2]}")
print(f"Yüzdesel artışa göre 2023 Tahmini // 20: {round(siralama_2022-(siralama_2022/100*yuzdelik_farklar[0]))} // 21: {round(siralama_2022-(siralama_2022/100*yuzdelik_farklar[1]))} // 22: {round(siralama_2022-(siralama_2022/100*yuzdelik_farklar[2]))}")

with open("results.txt","a", encoding="UTF-8") as f:
    f.write(f"{name} / Yüzdesel: {round(siralama_2022-(siralama_2022/100*yuzdelik_farklar[2]))} / Sayısal: {siralama_2022-sayisal_farklar[2]}\n")


'''
ÖRNEK VERİ GİRİŞİ
itü pc 1179 1821 2450 2580
boun pc 315 327 341 429
bilkent pc 350 432 602 722
odtü pc 878 1048 1170 1488
özyeğin pc 1326 1871 2660 2983
tobb pc 1578 2059 2860 3540
yeditepe pc 2851 4744 6990 8345
galatasaray pc 3131 4351 5590 6507
hacettepe pc 3576 5248 7200 11743
itü yapayzeka 1686 2861 4200 4200
boun endüstri 1448 1617 1260 1206
'''