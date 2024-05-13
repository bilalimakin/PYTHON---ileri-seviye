"""

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





x  = input("1. Sayı:")
y  = input("2. Sayı:")

print(type(x))              # x değerinin str değer olduğunu vericektir
print(type(y))              # y değerinin str değer olduğunu vericektir

toplam = x + y

print( toplam )             # burada x ve y değerleri str olduğundan birleştirme işlemi yapıcaktır.

x = int(x)                  ## x  değerini int çevirdik.
y = int(y)                  ## y  değerini int çevirdik.

toplam = x + y    

print(type(x))              # x değerinin int değer olduğunu vericektir
print(type(y))              # y değerinin int değer olduğunu vericektir

print( toplam )             # burada x ve y değerleri int olduğunda toplama işlemi yapıcaktır.



#Yarı çapı verilen bir dairenin Alan ve Çevre hesaplamalarını yapalım. 

'''

# Dairenin Alanı      :   πr²
# Dairenin çevresi    :   2πr

'''

pi = 3.14

r = float(input("Dairenin yarı Çapını girin : "))


alan    = pi * ( r ** 2)  # πr²

print(type(alan))

cevre   = 2 * pi * r     # 2πr

print(type(cevre))


print("Alan : " + str(alan))
print("Çevre : " + str(cevre))






Name = 'Bilal'
Surname = 'AKIN'
Age = 29

print( "My name is " + Name + " " + Surname + " and  \nI am " + str(Age) + " years old." )



Name = 'Bilal'

print(Name[len(Name)-1])
print(Name[-1])
print(Name[1:3])
print(Name[1:])
print(Name[:3])

Name = 'Bilal AKIN'

print(Name[1:10:2])

Name = 'Bilal'
Surname = 'AKIN'

print('My name is {} {}'.format(Name, Surname))




"""