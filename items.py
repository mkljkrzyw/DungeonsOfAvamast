from characters import Player
from ui import wypisz
def piwo(Player):
    wypisz("Pijesz piwo i czujesz się odświeżony.")
    if Player.hp + 5 > Player.max_hp:
        Player.hp = Player.max_hp
    else:
        Player.hp += 5