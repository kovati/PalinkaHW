import datetime
import random

from palinkas.palinka import Palinka
from storages.storage import Storage
#
# try:
#     palesz1 = Palinka(87, "Birs", 50, 2024, 4000)
#     palesz2 = Palinka(55, "Alma", 30, 2023, 500)
# except ValueError as vex:
#     print(f"Valami nem ok:  {vex}")
# else:
#     print(palesz1)

kocsma = Storage()
# kocsma.add_palinka(palesz1)
# kocsma.add_palinka(palesz2)

def rnd_gyumi() -> str:
    gyumi_list: list[str] = ["alma", "korte", "birs", "meggy", "cseresznye", "som", "barack", "szolo", "sutotok",
                             "dio", "malna", "eper", "szeder", "fuge", "vegyes"]
    return gyumi_list[random.randint(0, len(gyumi_list)-1)]

def rnd_value(min: int, max = datetime.date.today().year) -> int:
    return random.randint(min, max)

def create_random_palesz() -> Palinka:
    return Palinka(rnd_value(30,87), rnd_gyumi(), rnd_value(0,50), rnd_value(min=2000), rnd_value(500, 10000))

for _ in range(20):
    kocsma.add_palinka(create_random_palesz())

print(kocsma)
print(f"ennyi db palesz van: {kocsma.__len__()}")
print(f"ennyi liter palesz van: {kocsma.quantity()}")
print(f"ures? : {kocsma.is_empty()}")
print(f"A kocsmaban levo osszes palesz ara: {kocsma.sum_price()} Ft")

sum_income = 0
for _ in range(50):
    rnd_palesz = kocsma.rnd_palinka()
    fele: int = rnd_palesz.mennyiseg / 2
    #print(f"(Eredeti menny.: {rnd_palesz.mennyiseg}, a fele: {round(fele)} * {rnd_palesz.ar} = {fele * rnd_palesz.ar} igy szumma: {sum_income + (fele * rnd_palesz.ar)}")
    rnd_palesz.mennyiseg = round(fele)
    sum_income += fele * rnd_palesz.ar

print(f"50 random palesz felenek elfogyasztasa utan a teljes bevetel: {sum_income} Ft")
print(f"Ez utan a kocsmaban megmaradt osszes palesz ara: {kocsma.sum_price()} Ft")