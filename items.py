from characters import Player
from ui import wypisz
def piwo():
    wypisz("Pijesz piwo i czujesz się odświeżony.")
    if Player.health + 5 > Player.max_health:
        Player.health = Player.max_health
    else:
        Player.health += 5