class Tabor:
    def __init__(self, sor:str):
        adatok=sor.strip().split(';')
        self.resztvevok=adatok[0]
        self.letszam=int(adatok[1])
        self.felugyelok=adatok[3]
        self.szobaszam=int(adatok[4])
        self.testsuly=int(adatok[5])
        self.magassag=float(adatok[6].replace(",","."))

taborok:list[Tabor]=[]

file=open("Táborozas.txt", "r")
file.readline()
for sor in file:
    taborok.append(Tabor(sor))
file.close()

print(f"1. feladat: Táborozók száma: {len(taborok)}")

x=0
for i in taborok:
    x+=i.magassag
print(f"2. feladat: Az átlag sebesség: {float(x/len(taborok)) :.2f} km/h")

y=0.0
index=0
for i in range(len(taborok)):
    if y<taborok[i].magassag:
        y=taborok[i].magassag
        index=i
print(f"3. feladat: a legmagasabb diák adatai\n\tSzobaszám: {taborok[index].szobaszam}\n\tTestsúly: {taborok[index].testsuly}\n\tMagasság: {taborok[index].magassag}\n\t")

stat={}
print("4. feladat: Statisztika")
for i in taborok:
    d=str(i.év//10)+"0s"
    if d in stat:
        stat[d]+=1
    else:
        stat[d]=1
for i in stat:
    print(f"\t{i} -> {stat[i]} db")