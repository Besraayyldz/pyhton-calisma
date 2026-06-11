#listeler

liste1 = [1,2,3,4,5]
print(type(liste1)) #list veri tipindedir veriler int olabilir
print(liste1) #[1, 2, 3, 4, 5] yazdirir

liste2 = ["besra","ayse","fatma"]   
print(type(liste2)) #list veri tipindedir veriler str olabilir
print(liste2) #["besra", "ayse", "fatma"] yazdirir

liste3 = [1,"besra",1.5,1223j]
print(type(liste3)) #list veri tipleri farkli da olabilri
print(liste3) #[1, "besra", 1.5, 1223j] yazdirir
print(len(liste3)) #4 yazdirir yani liste3 de 4 eleman var demektir
print(liste3[0]) #1 yazdirir yani liste3 un 0.indeksindeki eleman 1 dir
print(liste3[-1]) #1223j yazdirir yani liste3 un -1.indeksindeki eleman 1223j dir
print(liste3[1:3]) #["besra", 1.5]
print(liste3[1:]) #["besra", 1.5, 1223j]
print(liste3[:3]) #[1, "besra", 1.5]
print(liste3[:]) #[1, "besra", 1.5, 1223j] yani liste3 un tum elemanlarini yazdirir
liste3[0] = "merhaba" #liste3 un 0.indeksindeki elemani "merhaba" yapar
print(liste3) #["merhaba", "besra", 1.5, 1223j] yazdirir
liste3[1:4] = ["selam"] #liste3 un 1.indeksinden 4.indeksine kadar olan elemanlari "selam" yapar
print(liste3) #["merhaba", "selam"] yazdirir
liste3.insert(1,"nasilsin") #liste3 un 1.indeksine "nasilsin" ekler
print(liste3) #["merhaba", "nasilsin", "selam"] yazdirir
liste3.append("gorusuruz") #liste3 un sonuna "gorusuruz" ekler
print(liste3) #["merhaba", "nasilsin", "selam", "gorusuruz"] yazdirir

liste4 = [1,2,3,4,5]
liste3.extend(liste4) #liste3 un sonuna liste4 un elemanlarini ekler
print(liste3) #["merhaba", "nasilsin", "selam", "gorusuruz", 1, 2, 3, 4, 5] yazdirir
liste3.remove("selam") #liste3 un "selam" elemanini siler
print(liste3) #["merhaba", "nasilsin", "gorusuruz", 1, 2, 3, 4, 5] yazdirir
liste3.pop() #liste3 un son elemanini siler
print(liste3) #["merhaba", "nasilsin", "gorusuruz", 1, 2, 3, 4] yazdirir
liste3.pop(0) #liste3 un 0.indeksindeki elemanini siler
print(liste3) #["nasilsin", "gorusuruz", 1, 2, 3, 4] yazdirir
del liste3[0] #liste3 un 0.indeksindeki elemanini siler
print(liste3) #["gorusuruz", 1, 2, 3, 4] yazdirir
del liste3[1:4] #liste3 un 1.indeksinden 4.indeksine kadar olan elemanlarini siler
print(liste3) #["gorusuruz", 4] yazdirir
del liste3 #liste3 u tamamen siler
# print(liste3) #NameError: name 'liste3' is not defined yazdirir yani liste3 u siler ve liste3 u kullanamayiz
liste2.clear() #liste2 un tum elemanlarini siler
print(liste2) #[] yazdirir


liste5 = [6,7,4,5,10,8,9,1,2,3]
liste5.sort() #liste5 i kucukten buyuge siralar
print(liste5) #[1, 10, 2, 3, 4, 5, 6, 7, 8, 9, 'ali', 'ayse', 'fatma', 'veli'] yazdirir yani sayilari kucukten buyuge siralar ama str leri siralayamaz ve str leri sayilardan sonra siralar

liste6 = ["ali","Veli","ayse","fatma"]# BUYUK HARF KULLANIRSAN ONCE BUYUK HARF OLANLARI KENDI ARASINDA SIRALAR SONRA DIGERLERI
liste6.sort(key=str.lower)#ile tum harfleri kucuge cevirip siralar
liste6.sort()
print(liste6)
liste6.sort(reverse= True)#tersten siralar
print(liste6)
liste6.reverse()#en son elemandan basa dogru siralar buyuklugu kucuklugu onemli degil
print(liste6)
print('merhh')

liste6=liste1.copy()#liste1 i kopyliyie
print(liste6)
#ayni silemilist ile de gerceklestirebilirz
liste6 = list(liste5)
print(liste6)

liste7 = [1,2,3,'merhaba']
liste8=liste7 +liste6#ciktisi[1, 2, 3, 'merhaba', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] olur
print(liste8)
#ayni islemi appent ile yapabiliriz
print(liste7)
liste1.append(liste7)
print(liste1)








