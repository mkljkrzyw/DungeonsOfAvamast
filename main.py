import os
from ui import wypisz, help, bestiariusz
from monsters import kukla_treningowa, rapax
from fights import walka

def main(player):
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
        "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę, kukłę treningową oraz drzwi prowadzące do korytarza...",
        #Nagle atakuje cię Rapax. Jego ostre szpony przebijają twoją skórę, a jego pazury tną głęboko. Zanim zdążysz zareagować czujesz nagły ból, a potem wszystko staje się białe.
        "objects": ["lawka", "kukla treningowa"],
        "south": "Korytarz"
    }
    }
    os.system("cls")
    wypisz("Budzisz się na niewygodnym materacu w ciemnym pomieszczeniu. Jesteś w południowej wieży w Thalindorze. Czujesz jedynie mróz i wilgoć. Widzisz przed sobą drzwi, które prowadzą na korytarz. Co robisz?", slowo_bold="drzwi", slowo_kolor={"drzwi": "YELLOW"})
    while True:
        avaiable_directions = []
        for i in rooms[currentRoom]:
            if i in directions:
                avaiable_directions.append(i)
        wypisz(f"\n --- {currentRoom} ---", styl="BOLD", kolor="GREEN")
        wypisz(f"\n" + rooms[currentRoom]["description"])
        if "objects" in rooms[currentRoom]:
            wypisz(f"\nObiekty: {', '.join(rooms[currentRoom]['objects'])}", slowo_bold=rooms[currentRoom]["objects"], slowo_kolor={obj: "YELLOW" for obj in rooms[currentRoom]["objects"]})
        wypisz(f"Dostępne kierunki: {', '.join(avaiable_directions)}", slowo_bold=avaiable_directions, slowo_kolor={dir: 'GREEN' for dir in avaiable_directions})
        turn = input("> ").strip()
        
        os.system("cls")
        turn = turn.split(" ", 1)
        komenda = turn[0].lower() if turn and turn[0] else ""
        argument = turn[1].strip().lower() if len(turn) > 1 else ""
        if komenda == "use":
            print("xd")
        elif komenda == "go":
            if not argument:
                wypisz("Nieznany kierunek.", kolor="RED")
            elif argument in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][argument]
            else:
                wypisz("Nie możesz iść w tym kierunku.", kolor="RED")
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
            wypisz("Nieznana komenda. Wpisz 'help' aby uzyskać listę dostępnych komend.", kolor="RED", slowo_kolor={"help": "CYAN"})