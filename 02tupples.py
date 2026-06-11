#TUPPLES verileri degistirilemez listeler degistirilebilirler
x=(1,2,3,"merhaba")
print(x[1])
print(x[3])
#x[1]=5 #hata verir cunku degistirilemezler
y=list(x) #tuppleri listeye cevirdik
y[1]=5 #listeler degistirilebilirler
print(y)

x=tuple(y) #listeyi tekrar tupplere cevirdik
print(x)

print("mrt")
(z,t,e,r)=x #tupplerdeki degerleri tek tek degiskenlere atayabiliriz
print(e)
(z,t,*e)=x #tupplerdeki degerleri tek tek degiskenlere atayabiliriz ama * ile kalan degerleri bir listeye atayabiliriz
print(e)

q= (93,2,5,1,6)
u=q+x #tuppleri birlestirebiliriz
print(u)    
u=q*4 #tuppleri tekrar edebiliriz
print(u)
print(u.count(1)) #tupplerdeki bir degerin kac kere gectigini sayar
print(u.index(93)) #tupplerdeki bir degerin ilk gectigi indexi verir

 
  