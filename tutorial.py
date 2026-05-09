import os
import sys
import time
import colorama
from characters import Player

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

colorama.just_fix_windows_console()
os.system("cls")
def help():
    print('''
Dungeons of Avamast
=================
Commands:
    go [direction]
    get [item]
    use [item]
    inventory 
    stats
    info
    help
''')

def tutorial(player):
    currentRoom = "Sypialnia"
    directions=["north", "south", "east", "west"]
    avaiable_directions = []
    rooms = {
    "Sypialnia": {
        "description": "Jesteś w swojej sypialni. Widzisz łóżko, skrzynię, drzwi prowadzące na korytarz oraz kartkę zawieszoną na ścianie.",
        "objects": ["skrzynia","kartka"],
        "items_available": "piwo",
        "west": "Korytarz"
    },
    "Korytarz": {
        "description": "Stoisz na korytarzu. Widzisz drzwi prowadzące do sypialni oraz drzwi prowadzące na dziedziniec",
        "east": "Sypialnia",
        "north": "dziedziniec"
    },
    "dziedziniec": {
        "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę oraz drzwi prowadzące do korytarza... \n \n Nagle atakuje cię Rapax. Jego ostre szpony przebijają twoją skórę, a jego pazury tną głęboko. Zanim zdążysz zareagować czujesz nagły ból, a potem wszystko staje się białe.",
        "south": "Korytarz"
    }
    }
    
    os.system("cls")
    help()
    wypisz("Budzisz się w swoim pokoju, w dobrze znanej twierdzy Ezelthorn. Coś jednak wydaje się nie tak. Wszystko jest ciche, a ty nie pamiętasz, co się stało. Musisz znaleźć sposób, by wydostać się z tej sytuacji.")
    while True:
        avaiable_directions = []
        for i in rooms[currentRoom]:
            if i in directions:
                avaiable_directions.append(i)
        wypisz("\n" + rooms[currentRoom]["description"])
        wypisz(f"\nDostępne kierunki: {', '.join(avaiable_directions)}")
        turn = input("> ")
        
        os.system("cls")
        turn = turn.split(" ",1)
        if turn[0]=="use":
            if "objects" in rooms[currentRoom] and turn[1] in rooms[currentRoom]["objects"]:
                if turn[1] == "skrzynia":
                    wypisz("Otwierasz skrzynię i znajdujesz piwo. Dodajesz je do swojego ekwipunku.")
                    player.inventory.append(rooms[currentRoom]["items_available"])
                    rooms[currentRoom]["items_available"] = None
                    rooms[currentRoom]["objects"].remove(turn[1])
                elif turn[1] == "kartka":
                    wypisz("Czytasz kartkę, a na niej napisane jest - 'Aby uzyskać pomoc odnośnie komend, wpisz 'help''.")
                    rooms[currentRoom]["objects"].remove(turn[1])
            else:
                wypisz(f"Nie ma tutaj {turn[1]}.")
        elif turn[0]=="go":
            if turn[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][turn[1]]
            else:
                wypisz("Nie możesz iść w tym kierunku.")
        elif turn[0]=="inventory":
            wypisz("Ekwipunek: " + str(player.inventory))
        elif turn[0]=="stats":
            player.show_stats()
        elif turn[0]=="help":
            help()
        elif turn[0]=="info":
            wypisz("Aktualna lokalizacja: " + currentRoom)
            wypisz(rooms[currentRoom]["description"])

        else:
            wypisz("Nieznana komenda. Wpisz 'help' aby uzyskać listę dostępnych komend.")