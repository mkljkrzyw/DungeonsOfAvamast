import os
from walki.encounters import encounter_check
from interfejs.ui import wypisz, help, sformatuj_ekwipunek
from lokacje.lokacjewiz import *
from lokacje.mapa import *
from zadania.quests import *
from przedmioty.weapons import krotki_miecz
from komendy.get import handle_get
from komendy.talk import handle_talk
from komendy.use import handle_use
def main(player):
    player.hp=player.max_hp
    player.inventory=[]
    player.weapon=krotki_miecz()
    player.energy=player.max_energy
    palisie=False
    tob_location = "hidden"
    tob1=False
    tob2=False
    kowal1=False
    stolyust=False
    podlogac=False
    # currentRoom = "Sala Sypialniana"
    # Lista lub zbiór odwiedzonych pokoi
    visited_rooms = set()
    # Na starcie dodajemy pokój, w którym gracz zaczyna
    currentRoom = "Sala Sypialniana"
    visited_rooms.add(currentRoom)
    os.system("cls")
    wypisz("Gwałtownie wyskakujesz z niewygodnego materacu w jasnym pomieszczeniu. Jesteś w południowej wieży w Thalindorze. Czujesz jedynie mróz i wilgoć. Widzisz przed sobą drzwi, które prowadzą na korytarz. Sen który miałeś wydawał się tak realny, że nie jesteś jeszcze pewien, czy to był tylko sen. Nie pamiętasz z niego praktycznie nic, ale również nie pamiętasz po co tutaj jesteś")
    while True:
        if currentRoom == "(0,0)":
            wieza()
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
        pokaz_minimape(currentRoom, rooms, visited_rooms)
        turn = input("> ").strip()
        while turn=="":
            turn = input()
        os.system("cls")
        turn = turn.split(" ", 1)
        komenda = turn[0].lower() if turn and turn[0] else ""
        argument = turn[1].strip().lower() if len(turn) > 1 else ""
        if komenda == "use":
            palisie, tob1, stolyust, podlogac = handle_use(
                player,
                currentRoom,
                rooms,
                quests,
                argument,
                palisie,
                tob1,
                stolyust,
                podlogac,
            )
        #elif komenda == "go":
        #    if not argument:
        #        wypisz("Nieznany kierunek.", kolor="RED")
        #    elif argument in rooms[currentRoom]:
        #        currentRoom = rooms[currentRoom][argument]
        #    else:
        #        wypisz("Nie możesz iść w tym kierunku.", kolor="RED")
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
            encounter_check(player, currentRoom)
        elif komenda == "get":
            handle_get(player, currentRoom, rooms, argument)
        elif komenda == "talk":
            tob_location, tob1, tob2, kowal1 = handle_talk(
                player,
                currentRoom,
                rooms,
                quests,
                argument,
                tob_location,
                tob1,
                tob2,
                kowal1,
            )
        elif komenda == "inventory":
            wypisz("Ekwipunek: " + sformatuj_ekwipunek(player.inventory))
        elif komenda == "stats":
            player.show_stats()
        elif komenda == "help":
            help()
        elif komenda == "info":
            wypisz("Aktualna lokalizacja: " + currentRoom)
            wypisz(rooms[currentRoom]["description"])
        else:
            wypisz("Nieznana komenda. Wpisz 'help' aby uzyskać listę dostępnych komend.", kolor="RED", slowo_kolor={"help": "CYAN"})
        for quest_key, quest_data in quests.items():
            if not isinstance(quest_data, dict):
                continue
            if quest_data.get("active") and quest_data.get("completed"):
                exp_reward = int(quest_data.get("exp", 0))
                item_reward = quest_data.get("items", "")
                gold_reward=quest_data.get("gold",0)
                player.exp += exp_reward
                if gold_reward:
                    player.gold += gold_reward
                    if item_reward:
                        wypisz(f"Zadanie '{quest_data.get('name', quest_key)}' zostało ukończone! Otrzymujesz {exp_reward} doświadczenia, {gold_reward} złota oraz {item_reward}!", kolor="GREEN")
                        player.inventory.append(item_reward)
                    else:
                        wypisz(f"Zadanie '{quest_data.get('name', quest_key)}' zostało ukończone! Otrzymujesz {exp_reward} doświadczenia i {gold_reward} złota!", kolor="GREEN")
                else:
                    if item_reward:
                        wypisz(f"Zadanie '{quest_data.get('name', quest_key)}' zostało ukończone! Otrzymujesz {exp_reward} doświadczenia oraz {item_reward}!", kolor="GREEN")
                        player.inventory.append(item_reward)
                    else:
                        wypisz(f"Zadanie '{quest_data.get('name', quest_key)}' zostało ukończone! Otrzymujesz {exp_reward} doświadczenia", kolor="GREEN")

                quest_data["active"] = False
        if player.exp >= player.expto_next_level:
            player.level += 1
            player.exp -= player.expto_next_level
            player.expto_next_level = int(player.expto_next_level * 1.5)
            player.max_hp += 20
            
            wypisz(f"Gratulacje! Awansowałeś na poziom {player.level}! Wybierz statystyke do ulepszenia:", kolor="GREEN")
            wypisz("1. Siła", slowo_bold="1.")
            wypisz("2. Zręczność", slowo_bold="2.")
            wypisz("3. Inteligencja", slowo_bold="3.")
            choice = input("> ").strip()
            if choice == "1":
                player.strength += 5
                player.max_hp += 10
            elif choice == "2":
                player.dexterity += 5
            elif choice == "3":
                player.intelligence += 5
                player.max_energy += 10
            player.energy = player.max_energy
            player.hp = player.max_hp


