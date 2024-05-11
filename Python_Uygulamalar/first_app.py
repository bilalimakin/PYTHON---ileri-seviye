# Metin ve Sayı Yazdırma
print("Merhaba")

print(2023+1)


# Matematiksel Operatörler
print(12+5)
print(12-5)
print(12/5)
print(12*5)
print(12**5)
print(12%5)
print(12//5)


# Değişken Tanımlama

## Birinci Yaklaşım
dukkanGelir = 1000 
dukkanKira = 150
PersonelMaas = 150
dukkanVergi = 0.27
dukkanGider = 250.23

Adi = "Bilal"
Soyadi = "AKIN"


netKar = dukkanGelir - ( dukkanVergi * ( dukkanKira + PersonelMaas + dukkanGider ) )
IsletmeSahibi = Adi + Soyadi

print(IsletmeSahibi) 

print(netKar)

## İkinci Yaklaşım
dukkanGelir, dukkanKira, PersonelMaas, dukkanVergi, dukkanGider, Adi, Soyadi = ( 1000, 150, 150, 0.27, 250.23, "Bilal", "AKIN" )

netKar = dukkanGelir - ( dukkanVergi * ( dukkanKira + PersonelMaas + dukkanGider ) )
IsletmeSahibi = Adi + Soyadi

print(IsletmeSahibi) 

print(netKar)











