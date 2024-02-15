import random

from palinkas.palinka import Palinka

class Storage:
    def __init__(self):
        self.__palinka_list: list["Palinka"] = []

    def quantity(self) -> float:
        sum_quantity: float = 0.0
        for p in self.__palinka_list:
            sum_quantity += p.mennyiseg
        return (sum_quantity / 10)

    def sum_price(self) -> int:
        sum_price: int = 0
        for p in self.__palinka_list:
            sum_price += p.ar * p.mennyiseg
        return sum_price

    def add_palinka(self, palesz):
        self.__palinka_list.append(palesz)

    def delete(self):
        pass
    # delete_by_index

    def rnd_palinka(self) -> Palinka:
        return self.__palinka_list[random.randint(0, len(self.__palinka_list)-1)]
    def is_empty(self) -> bool:
        return len(self.__palinka_list) == 0

    def __len__(self) -> int:
        return len(self.__palinka_list)

    def __str__(self) -> str:
        str_list: str = ""
        for p in self.__palinka_list:
            str_list += f"{p} \n"
        return str_list