import os
from ui import wypisz



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
        wypisz("\n" + rooms[currentRoom]["description"], slowo_bold=rooms[currentRoom]["objects"] if "objects" in rooms[currentRoom] else None)
        wypisz(f"\nDostępne kierunki: {', '.join(avaiable_directions)}")
        turn = input("> ").strip()
        
        os.system("cls")
        turn = turn.split(" ", 1)
        komenda = turn[0].lower() if turn and turn[0] else ""
        argument = turn[1].strip().lower() if len(turn) > 1 else ""

        if komenda == "use":
            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'use skrzynia'.")
            elif "objects" in rooms[currentRoom] and argument in rooms[currentRoom]["objects"]:
                if argument == "skrzynia":
                    wypisz("Otwierasz skrzynię i znajdujesz piwo. Dodajesz je do swojego ekwipunku.")
                    player.inventory.append(rooms[currentRoom]["items_available"])
                    rooms[currentRoom]["items_available"] = None
                    rooms[currentRoom]["objects"].remove(argument)
                elif argument == "kartka":
                    wypisz("Czytasz kartkę, a na niej napisane jest - 'Aby uzyskać pomoc odnośnie komend, wpisz 'help''.")
                    rooms[currentRoom]["objects"].remove(argument)
            else:
                wypisz(f"Nie ma tutaj {argument}.")
        elif komenda == "go":
            if not argument:
                wypisz("Podaj kierunek, np. 'go north'.")
            elif argument in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][argument]
            else:
                wypisz("Nie możesz iść w tym kierunku.")
        elif komenda == "inventory":
            wypisz("Ekwipunek: " + str(player.inventory))
        elif komenda == "stats":
            player.show_stats()
        elif komenda == "help":
            help()
        elif komenda == "info":
            wypisz("Aktualna lokalizacja: " + currentRoom)
            wypisz(rooms[currentRoom]["description"])

        else:
            wypisz("Nieznana komenda. Wpisz 'help' aby uzyskać listę dostępnych komend.")