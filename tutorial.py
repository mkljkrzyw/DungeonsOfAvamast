import os
from ui import wypisz, help



os.system("cls")


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
    wypisz("Sterowanie w tej grze opiera się na wpisywaniu prostych komend tekstowych w terminalu. Podczas wypisywania tekstu, możesz kliknąć 'enter', żeby od razu wyświetlić cały tekst. W każdym pomieszczeniu możesz wykonywać różne akcje, takie jak poruszanie się, interakcja z przedmiotami czy sprawdzanie swojego ekwipunku. Oto podstawowe komendy, które będziesz używać podczas gry:", kolor="CYAN", styl="BOLD")
    help()
    wypisz("Na początku każdego pomieszczenia, zostanie wyświetlony jego opis oraz dostępne kierunki, w które możesz się udać. Aby poruszać się, użyj komendy 'go' wraz z kierunkiem, np. 'go north'.", slowo_kolor={"go": "GREEN"})
    wypisz("Aby wchodzić w interakcje z przedmiotami, użyj komendy 'use' wraz z nazwą przedmiotu, np. 'use skrzynia'.", slowo_kolor={"use": "GREEN"})
    wypisz("Możesz również sprawdzić swój ekwipunek za pomocą komendy 'inventory' oraz swoje statystyki za pomocą komendy 'stats'.", slowo_kolor={"inventory": "YELLOW", "stats": "YELLOW"})
    wypisz("Jeżeli będziesz potrzebować pomocy, zawsze możesz wpisać 'help', aby wyświetlić listę dostępnych komend.", slowo_kolor={"help": "CYAN"})
    wypisz("Teraz, gdy znasz już podstawy, czas rozpocząć swoją przygodę w Dungeons of Avamast! Powodzenia!", kolor="CYAN", styl="BOLD")
    wypisz("Naciśnij Enter, aby kontynuować...")
    input()
    os.system("cls")
    wypisz("Budzisz się w swoim pokoju, w dobrze znanej twierdzy Ezelthorn. Coś jednak wydaje się nie tak. Wszystko jest ciche, a ty nie pamiętasz, co się stało. Musisz znaleźć sposób, by wydostać się z tej sytuacji.")
    while True:
        avaiable_directions = []
        for i in rooms[currentRoom]:
            if i in directions:
                avaiable_directions.append(i)
        wypisz(f"\n --- {currentRoom()} ---", styl="BOLD", kolor="GREEN")
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
            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'use skrzynia'.", slowo_kolor={"use": "GREEN"})
            elif "objects" in rooms[currentRoom] and argument in rooms[currentRoom]["objects"]:
                if argument == "skrzynia":
                    wypisz("Otwierasz skrzynię i znajdujesz piwo. Dodajesz je do swojego ekwipunku.", slowo_kolor={"piwo": "YELLOW"})
                    player.inventory.append(rooms[currentRoom]["items_available"])
                    rooms[currentRoom]["items_available"] = None
                    rooms[currentRoom]["objects"].remove(argument)
                elif argument == "kartka":
                    wypisz("Czytasz kartkę, a na niej napisane jest - 'Aby uzyskać pomoc odnośnie komend, wpisz 'help''.", slowo_kolor={"help": "CYAN"})
                    rooms[currentRoom]["objects"].remove(argument)
                elif argument in player.inventory:
                    if argument == "piwo":
                        wypisz("Pijesz piwo i czujesz się odświeżony.", slowo_kolor={"piwo": "YELLOW"})
                        player.health = player.max_health
                        player.inventory.remove(argument)
                    else:
                        wypisz(f"Używasz {argument} z ekwipunku, ale nic się nie dzieje.", slowo_kolor={argument: "YELLOW"})
            else:
                wypisz(f"Nie ma tutaj, ani w twoim ekwipunku {argument}.", slowo_kolor={"argument": "RED"})
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