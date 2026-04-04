from characters import Player
from tutorial import tutorial
import os

skip_tutorial = ""

print("DUNGEONS OF AVAMAST")
print("Podaj imię swojego bohatera:")
player_name = input("> ")
print("Wybierz swoją główną cechę:")
print("1. Siła")
print("2. Zręczność")
print("3. Inteligencja")
choice = input("> ")
if choice == "1":
    strength = 15
    dexterity = 5
    intelligence = 5
elif choice == "2":
    strength = 5
    dexterity = 15
    intelligence = 5
elif choice == "3":
    strength = 5
    dexterity = 5
    intelligence = 15
else:
    strength = 10
    dexterity = 10
    intelligence = 10
os.system("cls")
print("Teraz wybierz swoje błogosławieństwo:")
print("1. Oczy przyszłości (pozwala zobaczyć ukryte pułapki, skarby i przyszłe ruchy przeciwników)")
print("2. Manipulacja krwią (pozwala tworzyć bronie z krwi, zwiększa obrażenia i szybkość ataku, pozwala się leczyć)")
print("3. Manipulacja ciężarem (Pozwala nosić najcięższe zbroje i broń, zwiększa obronę i obrażenia)")
blessing_choice = input("> ")
if blessing_choice == "1":
    blessing = "Oczy przyszłości"
elif blessing_choice == "2":
    blessing = "Manipulacja krwią"
elif blessing_choice == "3":
    blessing = "Manipulacja ciężarem"
else:    blessing = "Brak"
player = Player(player_name, strength, dexterity, intelligence, blessing)
os.system("cls")
player.show_stats()
print("="*30)
print("Czy chcesz pominąć samouczek? (tak/nie) ")
while skip_tutorial.lower() not in ["tak", "nie"]:
    print("Proszę wpisać 'tak' lub 'nie'.")
    skip_tutorial = input("> ")
    if skip_tutorial.lower() == "tak":
        print("Pominięto samouczek. Powodzenia w Dungeons of Avamast!")
    else:    
        tutorial(player)