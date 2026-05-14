import os
from ui import wypisz, help, bestiariusz
from monsters import kukla_treningowa, rapax
from fights import walka
from main import main
from items import piwo
from weapons import prosty_sztylet

os.system("cls")


def tutorial(player):
    currentRoom = "Sypialnia"
    directions=["north", "south", "east", "west"]
    avaiable_directions = []
    rooms = {
    "Sypialnia": {
        "description": "Jesteś w swojej sypialni. Widzisz łóżko, skrzynię, piwo stojące na stole, drzwi prowadzące na korytarz oraz kartkę zawieszoną na ścianie.",
        "objects": ["skrzynia","kartka"],
        "items_available": ["piwo"],
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
    wypisz("Siedzisz w swoim pokoju, w dobrze znanej twierdzy Ezelthorn. Coś jednak wydaje się nie tak. Wszystko jest ciche, a ty nie pamiętasz, co się stało. Musisz znaleźć sposób, by wydostać się z tej sytuacji. Czujesz że rozwiązanie zna kukła na dziedzińcu")
    while True:
        avaiable_directions = []
        for i in rooms[currentRoom]:
            if i in directions:
                avaiable_directions.append(i)
        wypisz(f"\n --- {currentRoom} ---", styl="BOLD", kolor="GREEN")
        wypisz(f"\n" + rooms[currentRoom]["description"])
        if "objects" in rooms[currentRoom]:
            wypisz(f"\nObiekty: {', '.join(rooms[currentRoom]['objects'])}", slowo_bold=rooms[currentRoom]["objects"], slowo_kolor={obj: "YELLOW" for obj in rooms[currentRoom]["objects"]})
        if "items_available" in rooms[currentRoom] and rooms[currentRoom]["items_available"]:
            wypisz(f"Przedmioty do podniesienia: {', '.join(rooms[currentRoom]['items_available'])}", slowo_bold=rooms[currentRoom]["items_available"], slowo_kolor={item: "YELLOW" for item in rooms[currentRoom]["items_available"]})
        wypisz(f"Dostępne kierunki: {', '.join(avaiable_directions)}", slowo_bold=avaiable_directions, slowo_kolor={dir: 'GREEN' for dir in avaiable_directions})
        turn = input("> ").strip()
        
        os.system("cls")
        turn = turn.split(" ", 1)
        komenda = turn[0].lower() if turn and turn[0] else ""
        argument = turn[1].strip().lower() if len(turn) > 1 else ""

        if komenda == "use":
            bronie = {
                "sztylet": prosty_sztylet
            }

            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'use skrzynia'.", slowo_kolor={"use": "GREEN"})
            elif "objects" in rooms[currentRoom] and argument in rooms[currentRoom]["objects"]:
                if argument == "skrzynia":
                    wypisz("Otwierasz skrzynię i znajdujesz sztylet. Dodajesz go do swojego ekwipunku.", slowo_kolor={"sztylet": "YELLOW"})
                    player.inventory.append("sztylet")
                    rooms[currentRoom]["objects"].remove(argument)
                elif argument == "kartka":
                    wypisz("Czytasz kartkę, a na niej napisane jest - 'Aby uzyskać pomoc odnośnie komend, wpisz 'help''.", slowo_kolor={"help": "CYAN"})
                    rooms[currentRoom]["objects"].remove(argument)
                elif argument == "lawka":
                    wypisz("Siadasz na ławce, ale nic się nie dzieje. Może powinieneś poszukać czegoś innego do interakcji?")
                elif argument == "kukla treningowa" or argument == "kukla":
                    wypisz("Atakujesz kukłę treningową. Pora na pierwszą walkę!")
                    wypisz("W trakcie walki będziesz miał do wyboru opcje ataku, użcia błogosławieństwa, użyć przedmiotu z ekwipunku, bronić się, unikać lub spróbować uciec. Wybierz swoją strategię mądrze, aby pokonać przeciwnika!", kolor="CYAN", styl="BOLD")
                    wypisz("Wybranie ataku daje do wyboru różne ataki, które zadają obrażenia w zależności od twojej głównej cechy. Użycie błogosławieństwa pozwala na specjalne akcje, które mogą zmienić przebieg walki. Obrona zmniejsza obrażenia otrzymywane od przeciwnika, unikanie daje szansę na całkowite uniknięcie ataku, a ucieczka pozwala na zakończenie walki, ale może nie zawsze być skuteczna.")
                    wypisz("Pamiętaj, że każda decyzja w walce ma swoje konsekwencje, więc wybieraj mądrze i dostosuj swoją strategię do sytuacji!")
                    wypisz("Naciśnij Enter, aby rozpocząć walkę...")
                    input()
                    walka(player, kukla_treningowa())
                    os.system("cls")
                    wypisz("Teraz wiesz już jak walczyć! Pora przetestować twoje umiejętności")
                    wypisz("Nagle słyszysz ryk dochodzący z dziedzińca. To Rapax, potężna bestia (możesz dowiedzieć się o nim więcej w bestiariuszu). Rzuca się na Ciebie z ogromną siłą. Wiesz, że to już raczej twój koniec, ale próbujesz walczyć o swoje życie!")
                    walka(player, rapax())
                    wypisz("Czujesz, że twoje siły słabną, a obrażenia są coraz większe. W końcu Rapax zadaje ci ostatni cios, a ty widzisz nagle biel...")
                    wypisz("Naciśnij Enter, aby kontynuować...")
                    input()
                    main(player)
                    break
            elif argument in player.inventory:
                if argument == "piwo":
                    piwo()
                    player.inventory.remove(argument)
                elif argument == "bestiariusz":
                    bestiariusz()
                elif argument in bronie:
                    wybrana_bron = bronie[argument]()
                    wypisz("Ta broń to " + wybrana_bron.name + ". Jej główną cechą jest " + wybrana_bron.main_stat + ".", slowo_kolor={argument: "YELLOW"})
                    wypisz("Czy chcesz to wyposażyć? (tak/nie)", slowo_bold="tak/nie", slowo_kolor={"tak": "GREEN", "nie": "RED"})
                    odpowiedz = input("> ").strip().lower()

                    if odpowiedz == "tak":
                        player.weapon = wybrana_bron
                        if wybrana_bron.main_stat == "strength":
                            player.damage = wybrana_bron.damage * (player.strength // 3)
                        elif wybrana_bron.main_stat == "dexterity":
                            player.damage = wybrana_bron.damage * (player.dexterity // 3)
                        elif wybrana_bron.main_stat == "intelligence":
                            player.damage = wybrana_bron.damage * (player.intelligence // 3)
                        player.wzmocniony_dmg = player.damage
                        player.currentdmg = player.wzmocniony_dmg
                        wypisz(f"Wyposażasz {argument} i czujesz się silniejszy!", slowo_kolor={argument: "YELLOW"})
                    elif odpowiedz == "nie":
                        wypisz(f"Nie wyposażyłeś {argument}. Może przyda się później?", slowo_kolor={argument: "YELLOW"})
                    else:
                        wypisz("Proszę wpisać 'tak' lub 'nie'.", kolor="RED")
                else:
                    wypisz(f"Używasz {argument} z ekwipunku, ale nic się nie dzieje.", slowo_kolor={argument: "YELLOW"})
            else:
                wypisz(f"Nie ma tutaj, ani w twoim ekwipunku {argument}.", slowo_kolor={argument: "RED"})
        elif komenda == "get":
            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'get piwo'.", slowo_kolor={"use": "YELLOW"})
            elif argument in rooms[currentRoom].get("items_available", []):
                wypisz(f"Podnosisz {argument} i dodajesz go do swojego ekwipunku.", slowo_kolor={argument: "YELLOW"})
                player.inventory.append(argument)
                rooms[currentRoom]["items_available"].remove(argument)
            else:
                wypisz(f"Nie ma tutaj przedmiotu {argument}.", slowo_kolor={argument: "RED"})
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