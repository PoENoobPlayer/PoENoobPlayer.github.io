class Jatekok():
    def __init__(self,nev,ev,ar,platform):
        self.nev = nev
        self.ev = ev
        self.ar = ar
        self.platform = platform
fajl = open("videojatekok.txt", "r", encoding="utf-8")

videojatekok_listaja = []
for sorok in fajl:
    oszlop = sorok.strip().split("-")
    videojatekok_listaja.append(Jatekok(oszlop[0], oszlop[1], oszlop[2], oszlop[3]))

for item in videojatekok_listaja:
    print(f"Játék neve: {item.nev}, Kiadási év: {item.ev}, Ára: {item.ar}, Platformokon elérhető: {item.platform}")