import os
from ui import wypisz, help, bestiariusz
from monsters import kukla_treningowa, rapax
from fights import walka
from characters import Player
from weapons import *

def main(player):
    player.hp=player.max_hp
    player.inventory=["bestiariusz"]
    player.weapon=fists()
    player.energy=player.max_energy
    currentRoom = "Sala Sypialniana"
    directions=["north", "south", "east", "west", "enter", "exit"]
    avaiable_directions = []
    rooms = {
    "Sala Sypialniana": {
        "description": "Jesteś w dużym pomieszczeniu z wysokim sufitem, z niewielkich okien dociera słabe mocne światło spotęgowane śniegiem znajdującym się na dworze. Widzisz wiele twardych łóżek, stolik, oraz leżący na twoim notatnik. Na wschodzie znajdują się drzwi prowadzące do głównego holu",
        "objects": ["lozko","kartka"],
        "items_available": "piwo",
        "east": "Hol"
    },
    "Hol": {
        "description": "Stoisz w głównym holu, czujesz mróz. Widzisz nierozpalony kominek, zachodnie drzwi prowadzące do sali sypialnianej, połnocne drzwi prowadzące do biblioteki, wschodnie drzwi prowadzące do jadali, oraz wielkie drzwi na południu prowadzące na zewnątrz",
        "objects": ["kominek"],
        "west": "Sala Sypialniana",
        "north": "Biblioteka",
        "east": "Jadalnia",
        "south": "Dwor"
    },
    "Biblioteka":{
        "description": "Jesteś w bibliotece. Widzisz wiele regałów z książkami, biurko z krzesłem, oraz drzwi prowadzące do głównego holu",
        "objects": ["regały"],
        "south": "Hol"
    },
    "Jadalnia": {
        "description": "Jesteś w jadalni. Widzisz długi stół, kilka krzeseł, oraz drzwi prowadzące do głównego holu",
        "objects": ["stół"],
        "west": "Hol"
    },
    "Dwor": {
        "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę, kukłę treningową oraz drzwi prowadzące do korytarza...",
        "objects": ["lawka", "kukla treningowa"],
        "north": "Hol",
        "exit": "(0,0)"
    },
    #----MAPA ŚWIATA----
    


    "(0,0)": {
        "description": "Stoisz przed ogromną, ponurą wieżą. Rozciąga się stąd widok na mroźne pustkowia. Możesz wejść z powrotem do wieży wpisując 'wejdź'.",
        "enter": "Dwor", # Powrót do wieży
        "north": "(0,1)",
        "south": "(0,-1)",
        "east": "(1,0)",
        "west": "(-1,0)"

    },
    
    "(-2,2)": {
        "description": "Dotarłeś do bram tętniącego życiem Miasta. Słyszysz zgiełk kupców. Wpisz 'wejdź', aby wejść do miasta.",
        "enter": "Brama Miasta" # Przenosi do kolejnego zamkniętego "lochu"
    }
    }
    for x in range(-2, 3):
        for y in range(-2, 3):
            # Formatowanie ID pokoju dokładnie tak jak Twoje klucze (ze spacją)
            room_id = f"({x},{y})"

            # Jeśli pokoju o takich współrzędnych jeszcze NIE MA w słowniku, tworzymy pustkowie
            if room_id not in rooms:
                rooms[room_id] = {
                    "description": f"Przemierzasz zaśnieżone, puste pustkowia. Wiatr sypie ci śniegiem w oczy. (Współrzędne: {x}, {y})"
                }

            # Automatyczne dodawanie kierunków. 
            # Zapisujemy je do obecnego pokoju, niezależnie czy to wygenerowane pustkowie, czy unikalna lokacja jak (0, 0)
            if y < 2: rooms[room_id]["north"] = f"({x},{y+1})"
            if y > -2: rooms[room_id]["south"] = f"({x},{y-1})"
            if x < 2: rooms[room_id]["east"] = f"({x+1},{y})"
            if x > -2: rooms[room_id]["west"] = f"({x-1},{y})"
    os.system("cls")
    wypisz("Budzisz się na niewygodnym materacu w ciemnym pomieszczeniu. Jesteś w południowej wieży w Thalindorze. Czujesz jedynie mróz i wilgoć. Widzisz przed sobą drzwi, które prowadzą na korytarz. Co robisz?", slowo_bold="drzwi", slowo_kolor={"drzwi": "YELLOW"})
    while True:
        avaiable_directions = []
        for i in rooms[currentRoom]:
            if i in directions:
                avaiable_directions.append(i)
        wypisz(f"\n --- {currentRoom.upper()} ---", styl="BOLD", kolor="GREEN")
        wypisz(f"\n" + rooms[currentRoom]["description"])
        if "objects" in rooms[currentRoom]:
            wypisz(f"\nObiekty: {', '.join(rooms[currentRoom]['objects'])}", slowo_bold=rooms[currentRoom]["objects"], slowo_kolor={obj: "YELLOW" for obj in rooms[currentRoom]["objects"]})
        wypisz(f"Dostępne kierunki: {', '.join(avaiable_directions)}", slowo_bold=avaiable_directions, slowo_kolor={dir: 'GREEN' for dir in avaiable_directions})
        turn = input("> ").strip()
        while turn=="":
            turn = input()
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