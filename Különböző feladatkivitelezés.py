while True:
    a=int(input("Az első szám: "))
    if a==-1:
        break
    b=int(input("A második szám: "))
    if b==-1:
        break
osszeszorzas=1
for i in range(a,b+1):
    osszeszorzas*=i
print(f"A két szám közötti számok szorzata: {osszeszorzas}")



while True:
    a=int(input("Kérem az első számot: "))
    if a==-1:
        break
    b=int(input("Kérem a második számot: "))
    if b==-1:
        break
osszeg=0
for i in range(a,b+1):
    osszeg+=i
print(f"A két szám összege: {osszeg}")




print('1. feladat: Számok szorzata')
print('Kérem az alsó és a felső határt!')
a=int(input('a = '))
b=int(input('b = '))
if a>b:
    print('Az alsó határ kisebb legyen mint a felső!')
    while a>b:
        a=int(input('a = '))
        b=int(input('b = '))
        if a>b:
            print('Az alsó határ kisebb legyen mint a felső!')
        else:
            break
szorzat=1
for i in range(a,b+1):
    szorzat *= i
print(f'A számok szorzata {szorzat}')


print('1. feladat: Számok összeadása')
print('Kérem az alsó és felső határt!')
a=int(input('a = '))
b=int(input('b = '))
while a>b:
    print('Az alsó határ kisebb legyen mint a felső!')
    if a<b:
        break
    else:
        a=int(input('a = '))
        b=int(input('b = '))
osszeg=1
for i in range(a,b+1):
    osszeg += i
print(f'A számok összege: {osszeg}')




def szorzat(a,b):
    szorzas=a*b
    if szorzas<100:
        raise ValueError("A szorzat a megadott értéknél kisebb!")
    return szorzas

while True:
    a=int(input("Kérem az első számot: "))
    if a==0:
        break
    b=int(input("Kérem a második számot: "))
    if b==0:
        break
    try:
        print(f"A két szám szorzata: {szorzat(a,b)}")
    except ValueError as hiba:
        print(hiba)
