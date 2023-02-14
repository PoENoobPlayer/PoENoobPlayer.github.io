#1 Feladat: sorok megszámolása
with open("videojatekok.txt","r", encoding="utf-8") as jatekok:
    for sor in jatekok:
        print(len(sor.split("-")))
