
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
        self.inventory = []

    def show_stats(self):
        print(f"\n--- STATYSTYKI: {self.name} ---")
        print(f"Zdrowie: {self.hp}/{self.max_hp}")
        print(f"Złoto: {self.gold} monet")
        print(f"Poziom: {self.level}")
        print(f"Doświadczenie: {self.experience}")
        print(f"Siła: {self.strength}")
        print(f"Zręczność: {self.dexterity}")
        print(f"Inteligencja: {self.intelligence}")
        print(f"Błogosławieństwo: {self.blessing}")
        print("-" * 30)