import os
from books import bestie, kampania
from ui import wypisz, help, bestiariusz
from monsters import kukla_treningowa, rapax
from fights import walka
from characters import Player
from weapons import *

def main(player):
    player.hp=player.max_hp
    player.inventory=[""]
    player.weapon=fists()
    player.energy=player.max_energy
    palisie=False
    tob_location = "hidden"
    tob1=False
    tob2=False
    currentRoom = "Sala Sypialniana"
    directions=["north", "south", "east", "west", "enter", "exit"]
    avaiable_directions = []
    rooms = {
    "Sala Sypialniana": {
        "description": "Jesteś w dużym pomieszczeniu z wysokim sufitem, z niewielkich okien dociera mocne światło spotęgowane śniegiem znajdującym się na dworze. Widzisz wiele twardych łóżek, stolik, oraz leżący na twoim notatnik. Na wschodzie znajdują się drzwi prowadzące do głównego holu",
        "objects": ["lozko","kartka"],
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
        "objects": ["regaly"],
        "south": "Hol"
    },
    "Jadalnia": {
        "description": "Jesteś w jadalni. Widzisz długi stół, kilka krzeseł, oraz drzwi prowadzące do głównego holu",
        "objects": ["stol"],
        "west": "Hol"
    },
    "Dwor": {
        "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę, kukłę treningową oraz drzwi prowadzące do korytarza...",
        "objects": ["kukla treningowa"],
        "items_available": ["drewno"],
        #"characters": [""],
        "north": "Hol",
        "exit": "(0,0)"
    },
    #----Miasteczko----
    "Brama Miasteczka": {
        "description": "Wchodzisz do tętniącego życiem miasta. Widzisz kupców, rzemieślników, oraz mieszkańców. Możesz porozmawiać z kupcami, lub udać się na rynek.",
        "exit": "(-2,2)"
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
    
    "(2,2)": {
        "description": "Dotarłeś do bram spokojnego Miasteczka. Słyszysz rzadkie rozmowy, posępne rozmowy kupców.",
        "enter": "Brama Miasteczka", # Przenosi do kolejnego zamkniętego "lochu"
        "north": "(2,3)",
        "south": "(2,1)",
        "east": "(1,2)",
        "west": "(3,2)"
    }
    }
    for x in range(-3, 4):
        for y in range(-3, 4):
            # Formatowanie ID pokoju dokładnie tak jak Twoje klucze (ze spacją)
            room_id = f"({x},{y})"

            # Jeśli pokoju o takich współrzędnych jeszcze NIE MA w słowniku, tworzymy pustkowie
            if room_id not in rooms:
                rooms[room_id] = {
                    "description": f"Przemierzasz zaśnieżone, puste pustkowia. Wiatr sypie ci śniegiem w oczy. (Współrzędne: {x}, {y})"
                }

            # Automatyczne dodawanie kierunków. 
            # Zapisujemy je do obecnego pokoju, niezależnie czy to wygenerowane pustkowie, czy unikalna lokacja jak (0, 0)
            if y < 3: rooms[room_id]["north"] = f"({x},{y+1})"
            if y > -3: rooms[room_id]["south"] = f"({x},{y-1})"
            if x < 3: rooms[room_id]["east"] = f"({x+1},{y})"
            if x > -3: rooms[room_id]["west"] = f"({x-1},{y})"
    os.system("cls")
    wypisz("Gwałtownie budzisz się na niewygodnym materacu w jasnym pomieszczeniu. Jesteś w południowej wieży w Thalindorze. Czujesz jedynie mróz i wilgoć. Widzisz przed sobą drzwi, które prowadzą na korytarz. Sen który miałeś wydawał się tak realny, że nie jesteś jeszcze pewien, czy to był tylko sen. Nie pamiętasz z niego praktycznie nic, ale również nie pamiętasz po co tutaj jesteś")
    while True:
        if palisie:
            rooms["Hol"]["description"] = "Stoisz w głównym holu, czujesz ciepło. Widzisz rozpalony kominek, zachodnie drzwi prowadzące do sali sypialnianej, połnocne drzwi prowadzące do biblioteki, wschodnie drzwi prowadzące do jadali, oraz wielkie drzwi na południu prowadzące na zewnątrz"
            if tob_location=="hol":
                rooms["Hol"]["description"] = "Stoisz w głównym holu, czujesz ciepło. Widzisz rozpalony kominek, wygodny fotel, na którym siedzi zmęczony Tob, zachodnie drzwi prowadzące do sali sypialnianej, połnocne drzwi prowadzące do biblioteki, wschodnie drzwi prowadzące do jadali, oraz wielkie drzwi na południu prowadzące na zewnątrz"
            if tob_location == "hidden":
                tob_location = "dwor"
                rooms["Dwor"].setdefault("characters", [])
                if "Tob" not in rooms["Dwor"]["characters"]:
                    rooms["Dwor"]["characters"].append("Tob")
        avaiable_directions = []
        for i in rooms[currentRoom]:
            if i in directions:
                avaiable_directions.append(i)
        wypisz(f"\n --- {currentRoom.upper()} ---", styl="BOLD", kolor="GREEN")
        # Jeśli gracz otrzymał zadanie od Toba, ale jeszcze go nie wykonał, pokazuj przypomnienie w Holu
        #if currentRoom == "Hol" and tob1 and not tob2:
        #    wypisz("Tob: Miałeś posprzątać jadalnię. Nie zawracaj mi głowy, dopóki tego nie zrobisz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
        wypisz(f"\n" + rooms[currentRoom]["description"])
        if "objects" in rooms[currentRoom] and rooms[currentRoom]["objects"]:
            wypisz(f"\nObiekty: {', '.join(rooms[currentRoom]['objects'])}", slowo_bold=rooms[currentRoom]["objects"], slowo_kolor={obj: "YELLOW" for obj in rooms[currentRoom]["objects"]})
        if "items_available" in rooms[currentRoom] and rooms[currentRoom]["items_available"]:
            wypisz(f"Przedmioty do podniesienia: {', '.join(rooms[currentRoom]['items_available'])}", slowo_bold=rooms[currentRoom]["items_available"], slowo_kolor={item: "YELLOW" for item in rooms[currentRoom]["items_available"]})
        if rooms[currentRoom].get("characters"):
            wypisz(f"Postacie: {', '.join(rooms[currentRoom]['characters'])}", slowo_bold=rooms[currentRoom]["characters"], slowo_kolor={char: "YELLOW" for char in rooms[currentRoom]["characters"]})
        wypisz(f"Dostępne kierunki: {', '.join(avaiable_directions)}", slowo_bold=avaiable_directions, slowo_kolor={dir: 'GREEN' for dir in avaiable_directions})
        turn = input("> ").strip()
        while turn=="":
            turn = input()
        os.system("cls")
        turn = turn.split(" ", 1)
        komenda = turn[0].lower() if turn and turn[0] else ""
        argument = turn[1].strip().lower() if len(turn) > 1 else ""
        
        if komenda == "use":
            if argument == "kartka" and currentRoom == "Sala Sypialniana":
                wypisz("Na kartce napisane jest 'Wyszedłem po drzewo. Coś jeszcze powinno zostać na dworze. Rozpal w kominku, żebyśmy nie zamarźli.\n ~ Tob'")
            elif argument == "kominek" and currentRoom == "Hol":
                if "drewno" in player.inventory:
                    wypisz("Rozpalasz kominek, dając sobie trochę ciepła. Czujesz się bezpieczniej.")
                    player.inventory.remove("drewno")
                    rooms[currentRoom]["objects"].remove(argument)
                    palisie=True
                    wypisz("Słyszysz jakieś dźwięki dochodzące z zewnątrz. To musi być Tob", slowo_bold="Tob", slowo_kolor={"Tob": "YELLOW"})
                else:
                    wypisz("Nie masz nic, czym mógłbyś rozpalić kominek.")
            elif argument == "regaly" and currentRoom == "Biblioteka":
                wypisz("Przeglądasz regały i znajdujesz kilka interesujących książek. Co chcesz przeczytać?")
                wypisz("Co chcesz przeczytać? \n1. Bestiariusz \n2. VALANDORSKA KAMPANIA WOJENNA I JEJ KONSEKWENCJE \n3. Powrót" )
                choice = input("> ").strip()
                if choice == "1":
                    bestie()
                elif choice == "2":
                    kampania()
                elif choice == "3":
                    os.system("cls")
                    continue
            elif argument == "lozko":
                wypisz("Jest zbyt zimno żeby się położyć. Poza tym, nie masz czasu na drzemkę.")
            elif argument == "kukla treningowa" and currentRoom == "Dwor":
                wypisz("Podchodzisz do kukły treningowej i zaczynasz ją atakować, ćwicząc swoje umiejętności bojowe.")
                walka(player, kukla_treningowa)
            elif argument == "stol":
                wypisz("Stół jest solidny, ale nie wygląda na coś, co mógłbyś przenieść.")
        elif komenda == "go":
            if not argument:
                wypisz("Nieznany kierunek.", kolor="RED")
            elif argument in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][argument]
            else:
                wypisz("Nie możesz iść w tym kierunku.", kolor="RED")
        elif komenda == "get":
            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'get piwo'.", slowo_kolor={"use": "YELLOW"})
            elif argument in rooms[currentRoom].get("items_available", []):
                wypisz(f"Podnosisz {argument} i dodajesz go do swojego ekwipunku.", slowo_kolor={argument: "YELLOW"})
                player.inventory.append(argument)
                rooms[currentRoom]["items_available"].remove(argument)
            else:
                wypisz(f"Nie ma tutaj przedmiotu {argument}.", slowo_kolor={argument: "RED"})
        elif komenda == "talk":
            if not argument:
                wypisz("Podaj imię postaci, z którą chcesz porozmawiać, np. 'talk Tob'.", slowo_kolor={"talk": "GREEN"})
            elif "characters" in rooms[currentRoom] and argument in [char.lower() for char in rooms[currentRoom]["characters"]]:
                if argument == "tob" and currentRoom == "Dwor" and tob_location == "dwor":
                    wypisz("Tob: Hej, cieszę się, że się obudziłeś. Przyszedłem z nową dostawą drewna. Trochę mi to zajęło, ponieważ zaginął lokalny drwal, ale nie miałem czasu tego zbadać. W wolnym czasie idź do wioski, która znajduje się na północnym wschodzie i zobacz czy to coś poważnego. Idę do środka się ogrzać. Porozmawiamy później.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                    rooms["Dwor"]["characters"].remove("Tob")
                    # Jeśli już nie ma żadnych postaci na dworze, usuń klucz żeby nie wyświetlać nagłówka
                    if not rooms["Dwor"]["characters"]:
                        del rooms["Dwor"]["characters"]
                    rooms["Hol"].setdefault("characters", [])
                    if "Tob" not in rooms["Hol"]["characters"]:
                        rooms["Hol"]["characters"].append("Tob")
                    tob_location = "hol"
                elif argument == "tob" and currentRoom == "Hol" and tob_location == "hol":
                    # Conversation variations depending on quest state
                    if tob2:
                        wypisz("Tob: Dziękuję za posprzątanie jadalni. To dużo pomogło. Wiesz, że w bibliotece jest kilka książek, które mogą ci się przydać? Możesz tam zajrzeć, jeśli chcesz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                    elif tob1:
                        wypisz("Tob: Miałeś posprzątać jadalnię. Nie zawracaj mi głowy, dopóki tego nie zrobisz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                    else:
                        wypisz("Tob: Musimy zająć szykowaniem się wieży. Nie wiem, co się dzieje, ale coś jest nie tak, skoro nas tu wysłali. Podobno szykuje się jakaś duża bitwa. Zacznij od posprzątania jadalni. Muszę jeszcze trochę odpocząć, więc wróć do mnie jak skończysz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                        tob1=True
                else:
                    wypisz(f"Nie rozmawiać z {argument}.", slowo_kolor={argument: "RED"})
            else:
                wypisz(f"Nie ma tutaj postaci o imieniu {argument}.", slowo_kolor={argument: "RED"})
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