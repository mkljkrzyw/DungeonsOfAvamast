import os
from interfejs.ui import wypisz, help, bestiariusz, sformatuj_ekwipunek
from postacie.monsters import kukla_treningowa, rapax
from walki.fights import walka
from sceny.main import main
from przedmioty.items import piwo
from przedmioty.weapons import prosty_sztylet

os.system("cls")


def tutorial(player):
    visited_rooms = set()
    # Na starcie dodajemy pokój, w którym gracz zaczyna
    currentRoom = "Sypialnia"
    visited_rooms.add(currentRoom)
    os.system("cls")
    
    directions=["north", "south", "east", "west", "enter", "exit"]
    skroty_kierunkow = {
    "n": "north",
    "s": "south",
    "e": "east",
    "w": "west",
    "en": "enter",
    "ex": "exit"
    }
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
        "characters": ["Soren"],
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
    def pokaz_minimape(obecny_pokoj, slownik_pokoi, odwiedzone):
        if obecny_pokoj.startswith("("):
            return
        def sprawdz_kierunek(kierunek):
            if kierunek in slownik_pokoi[obecny_pokoj]:
                cel = slownik_pokoi[obecny_pokoj][kierunek]
                if cel.startswith("("):
                    return ""
                if cel in odwiedzone:
                    return f"[{cel}]"
                else:
                    return "[?]"
            return ""

        polnoc = sprawdz_kierunek("north")
        poludnie = sprawdz_kierunek("south")
        wschod = sprawdz_kierunek("east")
        zachod = sprawdz_kierunek("west")

        srodek_mapy = f"[* {obecny_pokoj} *]"

        # Ustawiamy stałe szerokości kolumn (siatka)
        L = 22  # szerokość lewej strony
        C = 28  # szerokość środka (Obecny pokój + pionowe linie)
        R = 22  # szerokość prawej strony

        # Całkowita szerokość mapy do wyśrodkowania tytułów
        szerokosc_mapy = L + 3 + C + 3 + R  

        # Tytuł ładnie wyśrodkowany
        print("\n" + "------------------------------ MAPA LOKALNA ------------------------------\n".center(szerokosc_mapy))

        # Rysujemy Północ
        if polnoc:
            print(" " * L + "   " + polnoc.center(C))
            print(" " * L + "   " + "|".center(C))

        # Sklejamy linię środkową wyrównując elementy do odpowiednich krawędzi
        # Zachód dociskamy do prawej (.rjust), Wschód dociskamy do lewej (.ljust), Środek centrujemy (.center)
        lewa_czesc = zachod.rjust(L) + (" - " if zachod else "   ")
        srodek = srodek_mapy.center(C)
        prawa_czesc = (" - " if wschod else "   ") + wschod.ljust(R)

        print(lewa_czesc + srodek + prawa_czesc)

        # Rysujemy Południe
        if poludnie:
            print(" " * L + "   " + "|".center(C))
            print(" " * L + "   " + poludnie.center(C))

        # Informacja o wyjściu
        if "exit" in slownik_pokoi[obecny_pokoj]:
            print("\n" + "* Dostępne wyjście w nieznane: 'exit' *".center(szerokosc_mapy))

        # Kreska zamykająca mapę
        print("-" * (szerokosc_mapy-3) + "\n")
    os.system("cls")
    wypisz("Sterowanie w tej grze opiera się na wpisywaniu prostych komend tekstowych w terminalu. Podczas wypisywania tekstu, możesz kliknąć 'enter', żeby od razu wyświetlić cały tekst. W każdym pomieszczeniu możesz wykonywać różne akcje, takie jak poruszanie się, interakcja z przedmiotami czy sprawdzanie swojego ekwipunku. Oto podstawowe komendy, które będziesz używać podczas gry:", kolor="CYAN", styl="BOLD")
    help()
    wypisz("Na początku każdego pomieszczenia, zostanie wyświetlony jego opis oraz dostępne kierunki, w które możesz się udać. Aby poruszać się, użyj komendy 'go' wraz z kierunkiem, np. 'go north'. można również używać skrótów, np. 'go n' lub nazw pokoi np. 'go dziedziniec'", slowo_kolor={"go": "GREEN"})
    wypisz("Aby wchodzić w interakcje z przedmiotami, użyj komendy 'use' wraz z nazwą przedmiotu, np. 'use skrzynia'.", slowo_kolor={"use": "GREEN"})
    wypisz("Możesz również sprawdzić swój ekwipunek za pomocą komendy 'inventory' oraz swoje statystyki za pomocą komendy 'stats'.", slowo_kolor={"inventory": "YELLOW", "stats": "YELLOW"})
    wypisz("W niektórych pomieszczeniach znajdują się postacie z którymi możesz porozmawiać, używając komendy 'talk' wraz z imieniem postaci, np. 'talk Soren'.", slowo_kolor={"talk": "GREEN"})
    wypisz("Jeżeli zdobędziesz jakąś broń lub zbroję, możesz ją wyposażyć używając komendy 'use' wraz z nazwą przedmiotu, np. 'use sztylet'.", slowo_kolor={"use": "GREEN", "sztylet": "YELLOW"})
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
        pokaz_minimape(currentRoom, rooms, visited_rooms)
        turn = input("> ").strip()
        while turn=="":
            turn = input()
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
                    wypisz("Otwierasz skrzynię i znajdujesz sztylet. Dodajesz go do swojego ekwipunku. (Teraz możesz sprawdzić zawartość ekwipunku za pomocą komendy 'inventory'. Aby wyposażyć sztylet, wpisz 'use sztylet')", slowo_kolor={"sztylet": "YELLOW"})
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
                    os.system("cls")
                    walka(player, kukla_treningowa())
                    os.system("cls")
                    wypisz("Teraz wiesz już jak walczyć! Pora przetestować twoje umiejętności")
                    wypisz("Nagle słyszysz ryk dochodzący z dziedzińca. To Rapax, potężna bestia (możesz dowiedzieć się o nim więcej w bestiariuszu). Rzuca się na Ciebie z ogromną siłą. Wiesz, że to już raczej twój koniec, ale próbujesz walczyć o swoje życie!")
                    wypisz("Naciśnij Enter, aby rozpocząć walkę...")
                    input()
                    os.system("cls")
                    walka(player, rapax())
                    wypisz("Czujesz, że twoje siły słabną, a obrażenia są coraz większe. W końcu Rapax zadaje ci ostatni cios, a ty widzisz nagle biel...")
                    wypisz("Naciśnij Enter, aby kontynuować...")
                    input()
                    
                    main(player)
                    break
            elif argument in player.inventory:
                if argument == "piwo":
                    piwo(player)
                    player.inventory.remove(argument)
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
        elif komenda == "talk":
            if not argument:
                wypisz("Podaj postać do rozmowy, np. 'talk Soren'.", slowo_kolor={"talk": "GREEN"})
            elif "characters" in rooms[currentRoom] and argument in [char.lower() for char in rooms[currentRoom]["characters"]]:
                if argument == "soren":
                    wypisz("Soren: Jak to z Tobą skończy, to zajme się Twoim ciałem", kolor="LIGHT_CYAN", slowo_bold="Soren")
                else:
                    wypisz(f"Rozmawiasz z {argument}, ale nie ma nic ciekawego do powiedzenia.", slowo_kolor={argument: "YELLOW"})
            else:
                wypisz(f"Nie ma tutaj postaci {argument}.", slowo_kolor={argument: "RED"})
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
            else:
                # Zamieniamy argument gracza na małe litery, żeby "Hol", "hol" i "HOL" działały tak samo
                argument = argument.lower()

                # ETAP 1: Czy gracz wpisał skrót? (np. "e" zamieniamy na "east")
                if argument in skroty_kierunkow:
                    argument = skroty_kierunkow[argument]

                # ETAP 2: Czy gracz wpisał poprawny kierunek? (np. "east")
                # Sprawdzamy czy wpisane słowo to kierunek i czy ten kierunek jest dostępny w obecnym pokoju
                if argument in directions and argument in rooms[currentRoom]:
                    currentRoom = rooms[currentRoom][argument]
                    visited_rooms.add(currentRoom)
                # ETAP 3: Czy gracz wpisał nazwę pokoju? (np. "hol")
                else:
                    znaleziono_cel = False
                    # Przeszukujemy wszystkie dostępne kierunki w obecnym pokoju
                    for kierunek in directions:
                        if kierunek in rooms[currentRoom]:
                            nazwa_pokoju = rooms[currentRoom][kierunek]

                            # Sprawdzamy czy nazwa pokoju z małych liter pasuje do wpisanego argumentu
                            if nazwa_pokoju.lower() == argument:
                                currentRoom = nazwa_pokoju
                                znaleziono_cel = True
                                visited_rooms.add(currentRoom)
                                break # Znaleźliśmy pokój, przerywamy pętlę
                            
                    # Jeśli pętla się skończyła i nic nie znaleźliśmy
                    if not znaleziono_cel:
                        wypisz("Nie możesz iść w tym kierunku ani do tego miejsca.", kolor="RED")
        elif komenda == "inventory":
            wypisz("Ekwipunek: " + sformatuj_ekwipunek(player.inventory))
        elif komenda == "stats":
            player.show_stats()
        elif komenda == "help":
            help()
        elif komenda == "info":
            wypisz("Aktualna lokalizacja: " + currentRoom)
            wypisz(rooms[currentRoom]["description"])
        elif komenda=="":
            print("")
            
        else:
            wypisz("Nieznana komenda. Wpisz 'help' aby uzyskać listę dostępnych komend.", kolor="RED", slowo_kolor={"help": "CYAN"})