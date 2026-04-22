from copy import copy
from situazione import Situazione
import datetime
class Percorso:
    def __init__(self, step:list):
        self.step = step
        self.costo=0
        self.calcola_costo()
    def __lt__(self, other):
        return self.costo < other.costo
    def calcola_costo(self):
        for i in range(len(self.step)):
            self.costo+=self.step[i].umidita
            if i==0 and self.step[i].localita!=self.step[i-1].localita: self.costo+=100
def risolviPercorso(dati):
    soluzioni=[]
    p=[]
    ricorsione(dati,soluzioni)
    for i in soluzioni:
        p.append(Percorso(i))
    for i in p:
        print(f"Costo: {i.costo}")
    return min(p).step, min(p).costo

def ricorsione(dati, soluzioni, solParz=[]):
    if not len(dati):
        soluzioni.append(copy(solParz))
    else:
        for i in dati[0]:
            if controllaStep(solParz,i):
                l=solParz.copy()
                l.append(i)
                ricorsione(dati[1:],soluzioni,l)

def controllaStep(sol:list, step:Situazione):
    c=step.localita
    cnt=0
    if not len(sol): return True
    for i in sol:
        if i.localita==c: cnt=cnt+1
    if cnt>=6: return False
    if sol[-1].localita==c: return True
    if len(sol)<3: return False
    if sol[-1].localita==sol[-2].localita==sol[-3].localita: return True
    return False
def main():
    meteoDao = [(Situazione(localita='Milano', data=datetime.date(2013, 1, 1), umidita=97), Situazione(localita='Torino', data=datetime.date(2013, 1, 1), umidita=73)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 2), umidita=79), Situazione(localita='Milano', data=datetime.date(2013, 1, 2), umidita=97), Situazione(localita='Torino', data=datetime.date(2013, 1, 2), umidita=85)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 3), umidita=66), Situazione(localita='Milano', data=datetime.date(2013, 1, 3), umidita=89), Situazione(localita='Torino', data=datetime.date(2013, 1, 3), umidita=73)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 4), umidita=75), Situazione(localita='Milano', data=datetime.date(2013, 1, 4), umidita=89), Situazione(localita='Torino', data=datetime.date(2013, 1, 4), umidita=60)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 5), umidita=81), Situazione(localita='Milano', data=datetime.date(2013, 1, 5), umidita=73), Situazione(localita='Torino', data=datetime.date(2013, 1, 5), umidita=51)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 6), umidita=86), Situazione(localita='Milano', data=datetime.date(2013, 1, 6), umidita=82), Situazione(localita='Torino', data=datetime.date(2013, 1, 6), umidita=52)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 7), umidita=82), Situazione(localita='Milano', data=datetime.date(2013, 1, 7), umidita=99), Situazione(localita='Torino', data=datetime.date(2013, 1, 7), umidita=65)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 8), umidita=72), Situazione(localita='Milano', data=datetime.date(2013, 1, 8), umidita=99), Situazione(localita='Torino', data=datetime.date(2013, 1, 8), umidita=96)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 9), umidita=73), Situazione(localita='Milano', data=datetime.date(2013, 1, 9), umidita=90), Situazione(localita='Torino', data=datetime.date(2013, 1, 9), umidita=94)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 10), umidita=72), Situazione(localita='Milano', data=datetime.date(2013, 1, 10), umidita=91), Situazione(localita='Torino', data=datetime.date(2013, 1, 10), umidita=88)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 11), umidita=64), Situazione(localita='Milano', data=datetime.date(2013, 1, 11), umidita=97), Situazione(localita='Torino', data=datetime.date(2013, 1, 11), umidita=93)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 12), umidita=63), Situazione(localita='Milano', data=datetime.date(2013, 1, 12), umidita=89), Situazione(localita='Torino', data=datetime.date(2013, 1, 12), umidita=99)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 13), umidita=74), Situazione(localita='Milano', data=datetime.date(2013, 1, 13), umidita=95), Situazione(localita='Torino', data=datetime.date(2013, 1, 13), umidita=89)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 14), umidita=64), Situazione(localita='Milano', data=datetime.date(2013, 1, 14), umidita=95), Situazione(localita='Torino', data=datetime.date(2013, 1, 14), umidita=89)),
(Situazione(localita='Genova', data=datetime.date(2013, 1, 15), umidita=76), Situazione(localita='Milano', data=datetime.date(2013, 1, 15), umidita=94), Situazione(localita='Torino', data=datetime.date(2013, 1, 15), umidita=90))]

    print(risolviPercorso(dati=meteoDao))


if __name__ == "__main__":
    main()