x=33
y=44

if x>y:
    print("x y den buyuktur")
elif x<y:
    print("x y den kucuktur")
else: 
    print("x y ye esittir")
#kosullu ifadelerle sozlukler
x=33
y=44
c=66

if not x>y and x>c:
    print("x en buyuktur")
elif y>c and y!=x:
    print("y en buyuktur")
elif c==y and c>x:
    print("c en buyuktur")

#ic ice kosullu ifadeler
x=33
y=44
if x>y:
    print("x y den buyuktur")
    if x%2==0:
        print("x cift sayidir")
    else:
        print("x tek sayidir")
elif x<y:
    print("x y den kucuktur")   
    if x%2==0:
        print("x cift sayidir")
    else:
        print("x tek sayidir")
else:
    print("x y ye esittir")
#pass dedigimizde iceri girer ama bisey dondurmez
if x>y:
    pass


