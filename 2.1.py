#a va b butun sonlari berilgan. Ularning bir vaqtda toq bolmasligi aniqlansin

a=int(input("a - qiymatini kiriting: "))
b=int(input("b - qiymatini kiriting: "))
if(a%2==0 and b%2==1):
    print(f'a={a} juft  b={b} toq. Ular bir vaqtda toq emas')
elif(a%2==1 and b%2==0):
    print(f'a={a} toq  b={b} juft. Ular bir vaqtda toq emas')
elif(a%2==1 and b%2==1):
    print('a va b bir paytda toq')
else:
    print('a va b juft')