from characters import Player
from ui import wypisz
def krew():
    if Player.hp < Player.max_hp:
        Player.hp += 20
        Player.energy -= 10
        wypisz("Używasz błogosławieństwa Krwi! Odzyskujesz 20 HP, ale tracisz 10 energii.", slowo_kolor={"20 HP": "LIGHT_GREEN", "10 energii": "YELLOW"})
    else:
        wypisz("Twoje zdrowie jest już pełne. Błogosławieństwo Krwi nie ma efektu.")
def oczy():
    Player.intelligence += 5
    Player.energy -= 10
    wypisz("Używasz błogosławieństwa Oczu! Zyskujesz 5 inteligencji, ale tracisz 10 energii.", slowo_kolor={"5 inteligencji": "LIGHT_GREEN", "10 energii": "YELLOW"})
def ciezar():
    Player.strength += 5
    Player.energy -= 10
    wypisz("Używasz błogosławieństwa Ciężaru! Zyskujesz 5 siły, ale tracisz 10 energii.", slowo_kolor={"5 siły": "LIGHT_GREEN", "10 energii": "YELLOW"})