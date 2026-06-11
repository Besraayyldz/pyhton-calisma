#veri tipleri
x=1
print(type(x)) #int veri tipindedir
x="besra"
print(type(x)) #str veri tipindedir 
x='besra '
print(type(x)) #str veri tipindedir 
x=1.5
print(type(x)) #float veri tipindedir
x=1223j
print(type(x)) #complex veri sayisal veri tiplerindendir karsimiza cok cikmaz

#mantiksal veri tipleri
q=True
print(type(q)) #bool veri tipindedir q degeri True da olabilir False da olabilir


#tuple veri tipleri
y=(1,2,3,4,5)
print(type(y)) #tuple veri tipindedirvy degeri 1 de 2 de 3 de 4 de 5 de olabilir
y=("besra","ayse","fatma")
print(type(y)) #tuple veri tipindedir y degeri besra da olabilir ayse de olabilir fatma da olabilir
y=(1,"besra",1.5,1223j)
print(type(y)) #tuple veri tipindedir y degeri 1 de olabilir besra da olabilir 1.5 de olabilir 1223j de olabilir

#list veri tipleri
x=[1,2,3,4,5]
print(type(x)) #list veri tipindedir x degeri 1 de olabilir 2 de olabilir 3 de olabilir 4 de olabilir 5 de olabilir
z=range(1,10)
print(type(z)) #range veri tipindedir z degeri 1 den 10 a kadar olabilir
print(z) #range(1, 10) yazdirir yani 1 den 10 a kadar olan sayilari yazdirmaz
print(list(z)) #range(1, 10) yazdirir yani 1 den 10 a kadar olan sayilari yazdirir

#dict veri tipleri
a={"name":"besra","age":20,"city":"istanbul"}
print(type(a)) #dict veri tipindedir a degeri name de olabilir age de olabilir city de olabilir
print(a) # {'name': 'besra', 'age': 20, 'city': 'istanbul'} yazdirir


binary=b"besra"
binaryArray=bytearray(5)
print(type(binary)) #bytes veri tipindedir binary degeri b"besra" olabilir
print(binary) #b"besra" yazdirir    
print(type(binaryArray)) #bytearray veri tipindedir binaryArray degeri bytearray(b"besra") olabilir 

#Casting= bir veri tipini baska bir veri turune cevirmek 
binary=b"besra"
binaryArray=memoryview(binary)
print(type(binaryArray)) #memoryview veri tipindedir binaryArray degeri memoryview(b"besra")olabilir
print(binary) #b"besra" yazdirir    

x= None
print(type(x)) #NoneType veri tipindedir x degeri None olabilir 
#casting
x=1
y=float(x) #int veri tipindeki x degerini float veri tipine cast ettik
print(y) #1.0 yazdirir  

y=str(12.5) #float veri tipindeki 12.5 degerini str veri tipine cast ettik
print(y) #12.5 yazdirir 
#print(y+1) #TypeError: can only concatenate str (not "int") to str yazdirir cunku y degeri str veri tipindedir ve 1 de int veri tipindedir bu iki veri tipi birbirine eklenemez

a="" \
"decwewewecwewdewed" \
"wedwedwedwedwedw" \
"wedwewedwewedwe" \
"wedwwedwedwed"
print(a) #decwewewecwewdewedwedwedwedwedwedwedwewedwewedwwedwedwed yazdirir 

b="""
wedwedw
wedwed
wedwedwedwed

"""

print(b) #wedwedw\nwedwed\nwedwedwedwed\n\n yazdirir yani \n karakteri yeni satir karakteridir ve \n karakteri gorunmez ama yeni satir olusturur

c="Merhaba Dunya    "
print(c[2:5]) #rha yazdirir 
print(c[:5]) #Merha yazdirir 
print(c[5:]) #ba Dunya yazdirir 
print(c[-5:]) #Dunya yazdirir 
print(c[::2]) #MraaDna yazdirir 
print(c[1::2]) #ehb uya yazdirir 
print(c.upper()) #MERHABA DUNYA yazdirir 
print(c.lower()) #merhaba dunya yazdirir 
print(c.replace("a","e")) #Merhebe Dunye yazdirir 

print(c.strip()) #bastaki ve sondaki boslukair siler

print(c.replace("M","D"))

d=a+b+c
print(d) #str yanina + yazarsan bosluksuz yan yana yazar int yanina + yazarsan toplama islemi yapar

f =22
d="benim yasim {}"
print(d.format(20)) #benim yasim 20 yazdirir
print(d,f) #benim yasim {} 22 yazdirir cunku d degeri str veri tipindedir ve f degeri int veri tipindedir bu iki veri tipi birbirine eklenemez ama print fonksiyonu ile yan yana yazdirilabilirler

e="benim yasim {} surada yasiyorum {}"
print(e.format(20, "Istanbul")) #benim yasim 20 surada yasiyorum Istanbul yazdirir
d="ankara"
print(e.format(f,d)) #benim yasim 22 surada yasiyorum ankara yazdirir

txt="mehmet bey'e"
print(txt) #mehmet bey'e yazdirir cunku tek tirnak icinde tek tirnak kullanilamaz ama cift tirnak icinde tek tirnak kullanilabilir
txt='mehmet bey\'e' 
print(txt) #mehmet bey'e yazdirir cunku tek tirnak icinde tek tirnak kullanilamaz ama cift tirnak icinde tek tirnak kullanilabilir ve tek tirnak icinde tek tirnak kullanmak istiyorsak o tek tirnak onune \ karakteri koyarak kullanabiliriz
txt="mehmet bey\\'e"
print(txt) #mehmet bey\'e yazdirir cunku tek tirnak icinde tek tirnak kullanilamaz ama cift tirnak icinde tek tirnak kullanilabilir ve tek tirnak icinde tek tirnak kullanmak istiyorsak o tek tirnak onune \ karakteri koyarak kullanabiliriz ve \ karakteri de \ karakteri ile kullanilirsa \ karakteri yazdirir

txt="mehmet bey\n'e"
print(txt) #mehmet bey
           #'e yazdirir \n alt satira gec demektir

txt="mehmet \bbey"
print(txt) #mehmetbey yazdirir \b karakteri backspace karakteridir yani bir karakter siler

print(10<9) #False yazdirir cunku 10 9 dan kucuktur demek yanlistir
print(10>9) #True yazdirir cunku 10 9 dan buyuktur demek dogrudur
print(10==9) #False yazdirir cunku 10 9 a esit demek yanlistir
print(bool(None)) #False yazdirir cunku None degeri False degerine esittir
print(bool(0)) #False yazdirir cunku 0 degeri False degerine esittir




