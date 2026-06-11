#degistirilebilir siralanabilir ama ayni elemanlari iceriinde bulundurmazlar
#sozlukler key-value seklinde degerleri tutarlar
x={"ad":"mert",
   "soyad":"yilmaz",
   "yas":25,
   "hobi":["voleybol","basketbol","cim bicmek"]
   }
print(x)
print(type(x))#dictionart yani sozluk oldugunu goruruz

#elemanlara erismek
y=x["ad"]
print(y)
#elemanlara bu sekilde de erisilebilir
y=x.get("soyad")
print(y)

# keys ile keylere erismek mumkun
z=x.keys()
print(z)
#valeu degerini degistirmek icin 
x["soyad"]="yag"
print(x)
#valeu degeri bu sekilde de degistirilebilr
x.update({"yas":"43"})
print(x)
#yeni key ekleme bu iki sekilde yapilabilir
x["fobi"]="asansor"
x.update({"unlu":"sertap erener"})
print(x)
#key silme
x.pop("hobi")#istenilen keyi siler
print(x)
del x ["soyad"]#bu islem de istenilen keyi siler
print(x)
x.popitem()#en sondaki keyi siler
print(x)
#x.clear()#butun sozlugu siler
print(x)

#sozluk koyalama
t=x.copy()
print(t)


diction = {
      "Liste0" : {
        "Yemek":"sarma",
        "Kahvalti":"yumurta"
    },
    "Liste2":{
        "Yemek":"borek",
        "Kahvalti":"zeytin"
    },
    "Liste3":{
        "Yemek":"et",
        "Kahvalti":"peynir"
    }


}

print(diction)#ile tum elemanara erisebiliriz
print(diction["Liste2"]["Yemek"])#istenilen veri degeri alinabilir


