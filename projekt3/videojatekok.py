#1 Feladat: sorok megszámolása
with open("videojatekok.txt","r", encoding="utf-8") as jatekok:
    jatekok = [j.strip().split("-") for j in jatekok]
# print(jatekok)
def jatekokszama(): 
    jatek = 0
    for jatek in jatekok:
            jatek = jatek +1
    print(f"A játékok száma:{jatek}")