#setler tupple gibi icerigi degistirilemez,siralamalari yoktur,elemanlara erisim saglanamaz
#set oldugunu belirtmek icin {} kullanilir ama dict ile karistirmamak gerekir
x={1,2,3,"merhaba"}
print(x)
#x[1] #hata verir cunku siralamalari yoktur 
y={1,2,3,"KELIME",5,2,True} #setlerde tekrar eden degerler olmaz true de 1 ile ayni kabul edilir cikti vermez
print(y)
print(type(y))#tipunun set oldugunu gosterir

z={"python","java","c++"}
y.update(z) #setleri birlestirmek icin update kullanilir
print(y)
print(z)

#ekleme islemi  
y.add("javascript") #setlere eleman eklemek icin add kullanilir
#silme islemi
y.remove("java") #setlerden eleman silmek icin remove kullanilir
print(y)
#birlestirme islemi
z=x.union(y) #setleri birlestirmek icin union kullanilir
print(z)
#pop, copy, clear gibi fonksiyonlar da setlerde kullanilir 
