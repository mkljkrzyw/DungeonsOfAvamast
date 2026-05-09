from characters import Player
from tutorial import tutorial
import os
import sys
import time
import colorama

colorama.init()

COLORS = {
    "RED": '\033[91m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
    "BLUE": '\033[94m',
    "PURPLE": '\033[95m',
    "CYAN": '\033[96m',
    "RESET": '\033[0m'
}
STYL = {
    "BOLD": '\033[1m',
    "UNDERLINE": '\033[4m',
    "NONE": '' # Pusty ciąg znaków, jeśli nie chcemy żadnego stylu
}

YELLOW = COLORS["YELLOW"]
GREEN = COLORS["GREEN"]
CYAN = COLORS["CYAN"]
RESET = COLORS["RESET"]

def wypisz(tekst, kolor="normalny", styl="brak", opoznienie=0.02, slowo_bold=None):
    kod_koloru = COLORS.get(kolor, COLORS["RESET"])
    kod_stylu = STYL.get(styl, STYL["NONE"])
    kod_reset = '\033[0m'
    
    # Nakładamy styl i kolor
    sys.stdout.write(kod_stylu + kod_koloru)
    
    # Jeśli chcemy pogrubić jedno słowo, piszemy słowo po słowie
    if slowo_bold:
        slowa = tekst.split()
        for i, slowo in enumerate(slowa):
            if slowo == slowo_bold:
                sys.stdout.write(STYL["BOLD"])
                for litera in slowo:
                    sys.stdout.write(litera)
                    sys.stdout.flush()
                    time.sleep(opoznienie)
                sys.stdout.write(STYL["NONE"])
            else:
                for litera in slowo:
                    sys.stdout.write(litera)
                    sys.stdout.flush()
                    time.sleep(opoznienie)
            if i < len(slowa) - 1:
                sys.stdout.write(" ")
    else:
        for litera in tekst:
            sys.stdout.write(litera)
        sys.stdout.flush()
        time.sleep(opoznienie)
        
    # Resetujemy wszystko na końcu
    sys.stdout.write(kod_reset + "\n")
    sys.stdout.flush()


skip_tutorial = ""
wyborstat=""
wyborblog=""
wyborimienia=""
wypisz("DUNGEONS OF AVAMAST", kolor="GREEN", styl="BOLD", opoznienie=0.01)
wypisz("Witaj w Dungeons of Avamast! Zanim rozpoczniesz swoją przygodę, musisz stworzyć swojego bohatera.", kolor="CYAN", styl="NONE", opoznienie=0.02)
while wyborimienia.lower() != "tak":
    wypisz("Podaj imię swojego bohatera:")
    player_name = input("> ")
    os.system("cls")
    wypisz(f"Twoje imię to {player_name}. Czy chcesz je zachować? (tak/nie)", kolor="YELLOW")
    wyborimienia = input("> ")
    os.system("cls")
while wyborstat.lower() != "tak":
    wypisz("Wybierz swoją główną cechę:")
    wypisz("1. Siła")
    wypisz("2. Zręczność")
    wypisz("3. Inteligencja")
    wypisz("inne - zrównoważony rozkład punktów")
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
        strength = 9
        dexterity = 8
        intelligence = 8
    os.system("cls")
    wypisz(f"Twoje statystyki to - Siła: {strength}, Zręczność: {dexterity}, Inteligencja: {intelligence}. Czy chcesz je zachować? (tak/nie)", kolor="YELLOW")
    wyborstat = input("> ")
    os.system("cls")
while wyborblog.lower() != "tak":
    wypisz("Teraz wybierz swoje błogosławieństwo:", opoznienie=0.01)
    wypisz("1. Oczy przyszłości (pozwala zobaczyć ukryte pułapki, skarby i przyszłe ruchy przeciwników)",opoznienie=0.01)
    wypisz("2. Manipulacja krwią (pozwala tworzyć bronie z krwi, zwiększa obrażenia i szybkość ataku, pozwala się leczyć)",opoznienie=0.01)
    wypisz("3. Manipulacja ciężarem (Pozwala nosić najcięższe zbroje i broń, zwiększa obronę i obrażenia)",opoznienie=0.01)
    wypisz("inne - brak błogosławieństwa",opoznienie=0.01)
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
    wypisz(f"Twoje błogosławieństwo to {blessing}. Czy chcesz je zachować? (tak/nie)", kolor="YELLOW")
    wyborblog = input("> ")
    os.system("cls")
player.show_stats()
wypisz("="*30)
wypisz("Czy chcesz pominąć samouczek? (tak/nie) ")
while skip_tutorial.lower() not in ["tak", "nie"]:
    wypisz("Proszę wpisać 'tak' lub 'nie'.")
    skip_tutorial = input("> ")
    if skip_tutorial.lower() == "tak":
        wypisz("Pominięto samouczek. Powodzenia w Dungeons of Avamast!")
    else:    
        tutorial(player)