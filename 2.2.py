#2.2 Ikkitа А vа B (А<B) butun sonlаri berilgаn. А vа B orаlig’idа joylаshgаn sonlаrni kаmаyish tаrtibidа (А vа B lаrni hаm hisobgа olgаn holdа) ekrаngа chiqаring, hаmdа ulаr sonini hisoblаng.

A=int(input("kichik sonni kiriting: A="))	
B=int(input("katta sonni kiriting: B="))
n=B-A+1
a=0
for i in range(0,n):
    print(B-i)
    a=a+1
print(f'{a} ta')