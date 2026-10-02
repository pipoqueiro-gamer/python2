n:int=int(input("digite um numero inteiro:"))
if n%2==0 and n%n==0:
    print(f'{n}:par')
else:
    print(f'{n}:impar')