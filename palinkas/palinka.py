class Palinka:
    def __init__(self, alkoholfok: int, gyumolcs: str, quantity: int, keszites_eve: int, price: int):
        self.__alkoholfok = self.__check_alc(alkoholfok)
        self.__gyumolcs = self.__check_fruit_name(gyumolcs)
        self.mennyiseg = quantity
        self.__keszites_eve = self.__check_year(keszites_eve)
        self.ar = price

    @property
    def ar(self):
        return self.__ar

    @ar.setter
    def ar(self, value):
        if value not in range(500, 10001):
            raise ValueError("Ar 500 es 10000 ft/deciliter kozott kell lennie")
        self.__ar = value

    @property
    def mennyiseg(self):
        return self.__mennyiseg

    @mennyiseg.setter
    def mennyiseg(self, value):
        if value not in range(0, 51):
            raise ValueError("A mennyiségnek 0-50 deciliter kozott kell lennie")
        self.__mennyiseg = value
        
    def __check_fruit_name(self, gyumolcs) -> str:
        if len(gyumolcs) not in range(0, 20):
            raise ValueError("Túl hosszú név!")
        return gyumolcs

    def __check_alc(self, alkoholfok) -> int:
        if alkoholfok not in range(30, 88):
            raise ValueError("Alkoholfoknak 30 es 87 kozott kell lennie!")
        return alkoholfok

    def __check_year(self, keszites_eve) -> int:
        if keszites_eve not in range(2000, 2025):
            raise ValueError("Készítés éve csak 2000-től lehet!")
        return keszites_eve

    def __str__(self) -> str:
        return f"A {self.__gyumolcs} palinka {self.__alkoholfok} fokos, {self.__keszites_eve}-ban keszult {self.__mennyiseg} dl mennyisegben. Ara: {self.ar} Ft"