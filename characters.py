from weapons import *
class Player:
    def __init__(self, name, strength, dexterity, intelligence, blessing):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.gold = 50
        self.level = 1
        self.experience = 0
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.blessing = blessing
        self.inventory = ["bestiariusz"]
        self.weapon = fists()
        self.energy = 10
        self.max_energy = 10
        if self.weapon.main_stat == "strength":
            self.damage = self.weapon.damage*(self.strength//3)
        elif self.weapon.main_stat == "dexterity":
            self.damage = self.weapon.damage*(self.dexterity//3)
        elif self.weapon.main_stat == "intelligence":
            self.damage = self.weapon.damage*(self.intelligence//3)

    def show_stats(self):
        print(f"\n--- STATYSTYKI: {self.name} ---")
        print(f"Poziom: {self.level}")
        print(f"Doświadczenie: {self.experience}")
        print(f"Zdrowie: {self.hp}/{self.max_hp}")
        print(f"Energia: {self.energy}/{self.max_energy}")
        print(f"Złoto: {self.gold} monet")
        print(f"Siła: {self.strength}")
        print(f"Zręczność: {self.dexterity}")
        print(f"Inteligencja: {self.intelligence}")
        print(f"Błogosławieństwo: {self.blessing}")
        print(f"bron: {self.weapon.name if self.weapon else 'Brak'}")
        print(f"Obrazenia: {self.damage}")
        print("-" * 30)