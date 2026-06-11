#ctrl+c ile donguden cikabilirsz
x=1
#while dongusu
while x<10:
    print(x)
    x+=1 #x=x+1 ile ayni islemi yapar
while True:
    print(x)
    if(x==15):
        print("x 15 e esittir")
        break #donguyu durdurur
    x+=1
x=1
while x<5:
    x+=1
    if x==3:
        continue #dongunun basina doner
    print(x)
else:
    print("dongu bitti")

#for dongusu
fruits=["elma","armut","muz","kivi"]
for i in fruits:
    print(i)

for x in "meyve":
    print(x)#m e y v e harflerini tek tek yazdirir

if "elma" in fruits:
    print("elma meyveler arasinda")
#kiviyi bulana kadar arar bulunca yazar
for i in fruits:
    if i=="kivi":
        print("kivi meyveler arasinda")
        break

#kiviyi bulana kadar arar bulunca yazar
for i in fruits:
    if i=="kivi":
        print("kivi meyveler arasinda")
        continue
    print(i)

#1 den 6 ya kadar sayilari yazar
for x in range(6):
    if x==2:
        continue
    print(x)
print("merhaba")

#2 den 6 ya kadar tum degerleri yazar
for x in range(2,6):
    print(x)

#2 den 6 ya kadar tum cift degerleri yazar
for x in range(2,6,2):
    print(x)  
else:
    print("dongu bitti")

#ic ice for
sayi=[1,2,3]
names=["mert yilmaz","ayse yilmaz"]
for i in sayi:
    for j in names:
        print(i,j)
 




