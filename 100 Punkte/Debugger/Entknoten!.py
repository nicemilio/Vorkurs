from enum import Enum
import random


class Types(Enum):
    FIRE: str = "Feuer"
    WATER: str = "Wasser"
    GRASS: str = "Pflanze"


weakness_matrix = {Types.FIRE: {Types.FIRE: 0.5,
                                Types.WATER: 2,#Switch water and grass
                                Types.GRASS: 0.5},
                   Types.WATER: {Types.FIRE: 0.5,
                                 Types.WATER: 0.5,
                                 Types.GRASS: 2},
                   Types.GRASS: {Types.FIRE: 2,
                                 Types.WATER: 0.5,#Switch water and fire
                                 Types.GRASS: 0.25}}


class Attack:
    def __init__(self, name: str, power: int, type: Types):
        self.name = name
        self.power = power
        self.type = type

    def __str__(self):
        return f"{self.name} - {self.type} - {self.power}"


# missing defense, items
class Pokemon:
    def __init__(self, name: str, health: int, attack: Attack, type: Types):
        self.name = name
        self.health = health
        self.full_health = health
        self.attack = attack
        self.type = type

    def __str__(self):
        return f"\n" \
               f"|- Name: {self.name}\n" \
               f"|- Typ: {self.type.value}\n" \
               f"|- Leben: {self.health}\n" \
               f"|- Attacke: {self.attack}\n"

    def heilen(self):
        self.health = self.full_health

    def wird_angriffen_von(self, pokémon):
        if not self.ist_am_leben():
            print(f"Dein Pokemon ist ohnmächtig und kann nicht weiter kämpfen.")
            return
        print(f"{self.name} wird von {pokémon.name} angegriffen.")
        print(f"{pokémon.name} führt {pokémon.attack.name} aus.")

        multiplikator = weakness_matrix[pokémon.type][self.type]
        damage = pokémon.attack.power * multiplikator
        if multiplikator >= 2:
            print(f"Es ist sehr effektiv.")
        elif multiplikator < 0.5:
            print(f"Es ist nicht sehr effektiv.")

        print(f"{self.name} nimmt {damage} Schaden.")
        self.health -= damage

        if not self.ist_am_leben():
            print(f"{self.name} wurde besiegt!")

    def ist_am_leben(self) -> bool:
        if self.health > 0:
            return True
        return False



def print_all(pokémon: list[Pokemon]):
    for p in pokémon:
        print(p)

if __name__ == '__main__':
    mehrere_pokémon = [Pokemon("Glumanda", 31, Attack("Glut", 5, Types.FIRE), Types.FIRE),
                       Pokemon("Bisasam", 31, Attack("Rankenhieb", 5, Types.GRASS), Types.GRASS),
                       Pokemon("Schiggy", 31, Attack("Aquaknarre", 5, Types.WATER), Types.WATER)]

    print_all(mehrere_pokémon)

    while all(pokémon.ist_am_leben() for pokémon in mehrere_pokémon):
        attack_pokémon_index = random.randint(0, len(mehrere_pokémon) - 1)
        defense_pokémon_index = random.randint(0, len(mehrere_pokémon) - 1)
        if attack_pokémon_index == defense_pokémon_index:
            continue
        attack_pokémon = mehrere_pokémon[attack_pokémon_index]
        defense_pokémon = mehrere_pokémon[defense_pokémon_index]
        defense_pokémon.wird_angriffen_von(attack_pokémon)

        print_all(mehrere_pokémon)