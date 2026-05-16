import os
from characters import Player
from ui import wypisz
uderzenie=False
zwiekszenie=False
unikanie=False
def krew(Player):
    global uderzenie, zwiekszenie
    if Player.energy >= 10:
        print("Używasz błogosławieństwa Krwi!")
        print("Wybierz efekt:")
        print("1. Odzyskaj 20 HP (10E)")
        print("2. Zwiększ obrażenia o 20% na 3 tury (10E)")
        print("3. Stwórz broń z krwi, która zada raz obrażenia równe 50% twojej aktualnej HP (10E)")
        choice = input("Wybierz opcję: ").strip()
        if choice == "1":
            if Player.hp +20 <= Player.max_hp:
                Player.hp += 20
                Player.energy -= 10
                os.system("cls")
                wypisz("Odzyskujesz 20 HP, ale tracisz 10 energii.", slowo_kolor={"20 HP": "LIGHT_GREEN", "10 energii": "YELLOW"})
            else:
                Player.hp = Player.max_hp
                Player.energy -= 10
                os.system("cls")
                wypisz("Twoje zdrowie jest już pełne. Błogosławieństwo Krwi nie ma efektu.")
        elif choice == "2":
            zwiekszenie=True
            Player.currentdmg *= 1.2
            Player.energy -= 10
            os.system("cls")
            wypisz("Zwiększasz obrażenia o 20% na 3 tury, ale tracisz 10 energii.", slowo_kolor={"20% obrażeń": "LIGHT_GREEN", "10 energii": "YELLOW"})
        elif choice == "3":
            uderzenie=True
            Player.wzmocniony_dmg = Player.hp * 0.5
            Player.energy -= 10
            os.system("cls")
            wypisz("Tworzysz broń z krwi, która zada raz obrażenia równe 50% twojej aktualnej HP, ale tracisz 10 energii.", slowo_kolor={"50% HP": "LIGHT_GREEN", "10 energii": "YELLOW"})
    else:
        wypisz("Nie masz wystarczająco energii, aby użyć błogosławieństwa Krwi!", slowo_kolor={"Nie masz wystarczająco energii, aby użyć błogosławieństwa Krwi!": "RED"})
def oczy(Player):
    global zwiekszenie, unikanie
    if Player.energy >= 10:
        print("Używasz błogosławieństwa Oczu Przyszłości!")
        print("Wybierz efekt:")
        print("1. Znajdź słabe punkty przeciwnika - zwiększ obrażenia o 20% na 3 tury (10E)")
        print("2. Zobacz następny ruch przeciwnika - automatycznie unikaj przez 3 tury (10E)")
        choice= input("Wybierz opcję: ").strip()
        if choice == "1":
            zwiekszenie=True
            Player.currentdmg *= 1.2
            Player.energy -= 10
            os.system("cls")
            wypisz("Znajdujesz słabe punkty przeciwnika, zwiększając obrażenia o 20% na 3 tury, ale tracisz 10 energii.", slowo_kolor={"20% obrażeń": "LIGHT_GREEN", "10 energii": "YELLOW"})
        elif choice == "2":
            unikanie=True
            Player.energy -= 10
            os.system("cls")
            wypisz("Zobaczysz następny ruch przeciwnika, automatycznie unikając przez 3 tury, ale tracisz 10 energii.", slowo_kolor={"3 tury": "LIGHT_GREEN", "10 energii": "YELLOW"})
    else:
        wypisz("Nie masz wystarczająco energii, aby użyć błogosławieństwa Oczu Przyszłości!", slowo_kolor={"Nie masz wystarczająco energii, aby użyć błogosławieństwa Oczu Przyszłości!": "RED"})
def ciezar(Player):
    global uderzenie
    if Player.energy >= 10:
        print("Używasz błogosławieństwa Manipulacji Ciężarem!")
        print("Przy następnym ataku zwiększysz ciężar broni, przez co zada 5 razy więcej obrażeń (10E)")
        uderzenie=True
        Player.wzmocniony_dmg = Player.damage * 5
        Player.energy -= 10
    else:
        wypisz("Nie masz wystarczająco energii, aby użyć błogosławieństwa Manipulacji Ciężarem!", slowo_kolor={"Nie masz wystarczająco energii, aby użyć błogosławieństwa Manipulacji Ciężarem!": "RED"})
    
        