import random
from lokacje.mapa import strefa_potworow, strefa_bandytow
from lokacje.mapa import *
from postacie.monsters import *
from walki.fights import *

def encounter_check(player, current_room):
    if not current_room.startswith("("):
        return
    chance = 1
    if current_room in strefa_potworow:
        if random.random() < chance:
            print("Spotykasz potwora!")
            walka(player, rapax)
    elif current_room in strefa_bandytow:
        if random.random() < chance:
            print("Spotykasz bandytę!")
            walka(player, bandyta)