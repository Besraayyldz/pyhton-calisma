#koda yorum # ile ilabilir 
"""
bu araya yazdiklarimizda yorum
olarak degerlendirilebilir
bumada cok satirli yorum diyebiliriz

"""
#yorum satirina almak istedigin metni secip ctrl / tiklarsan hepsini yprum yapar
#OPERATORLER
#Aritmetik operatorler= +  _  *  /  %  **  //
# matematik islemlerimi yapabildigimiz operatorler
X=100
Y=50
print(X+Y)
print(X-Y)
print(X*Y)
print(X/Y)
print(X//Y)#YAZDIGIMIZDA ONDALIKLI SONUC VERMEZ
print(X**Y)#x uzeri y yi verir
print(X%Y)# (bolumun kalani)

#denklik operatorleri
# = += -= *= /=
z=3
z = z+3
z+=3 #de ayni ifadedir
print(z)
z-=3#cikarma
print(z)
z*=3#carpma
print(z)
z/=3#bolme
print(z)
z%=4# kalani
print(z)
z**=4
print(z)
z=16.0
z//=4
print(z)

#karsialstirma operatorleri
x=1
y=2
print(x==y)#x vw y esit mi?
print(x!=y)#x vw y esitdegil mi?
print(x>y)#x y den buyuk  mi?
print(x<y)#x y den kucuk mi?
print(x<=y)#x vw y esit veya kucuk mu?


#mantiksal operatorler
#and or not
x=5
print(x>6 and x<10) #iki durumun da gecerli olasi gerekiyro
print(x>6 or x<10) #en az 1 durumun gecerli olasi gerekiyro
print(not(x>6 or x<10)) #icerdeki durumun degilini(tersini) alir 

#kimlik opaeratoreri
x = [1,2,3]
y = [1,2,3]
z=x
print(x is z)#x ve z ayni degerleri mi  true evet 
print(x is y)#x ve y ayni degerleri mi false x ve y farkli degerler

print(x is not z)#x ve z ayni degerleri mi bak degilini ver false evet 
print(x is not y)#x ve y ayni degerleri mi bak degilini ver true

#uyelik operatorleri
#in , not in
x=[1,2]
print(1 in x)#1 x in icerisinde mi? ture
print(5 in x)#1 x in icerisinde mi?FALSE
print(1 not in x)#1 x in icerisinde mi?FALSE

# BITWISE OPERATORLERI
#& | ^ 
print(6 & 3) # 6 nin binary karsiligi ile 3 un binary karsiligini veya leyip ondalik karsiligini veriyor
print(6 | 3) # 6 nin binary karsiligi ile 3 un binary karsiligini ve leyip ondalik karsiligini veriyor
print(6 ^ 3) # 6 nin binary karsiligi ile 3 un binary karsiligini xor leyip ondalik karsiligini veriyor

