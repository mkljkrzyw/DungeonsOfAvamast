import os

from wiedza.books import bestie, kampania
from walki.fights import walka
from lokacje.lokacjewiz import *
from lokacje.mapa import *
from postacie.monsters import dopler, kukla_treningowa, rapax
from zadania.quests import dziennik
from interfejs.ui import wypisz
from przedmioty.weapons import krotki_miecz, prosta_wlocznia, prosty_miecz_dwureczny


def handle_use(player, currentRoom, rooms, quests, argument, palisie, tob1, stolyust, podlogac):
    bronie = {
        "prosta wlocznia": prosta_wlocznia,
        "prosty miecz dwureczny": prosty_miecz_dwureczny,
    }

    if not argument:
        wypisz("Podaj obiekt do użycia, np. 'use skrzynia'.", slowo_kolor={"use": "GREEN"})
    elif "objects" in rooms[currentRoom] and argument in rooms[currentRoom]["objects"]:
        if argument == "kartka" and currentRoom == "Sala Sypialniana":
            wypisz("Na kartce napisane jest 'Wyszedłem po drzewo. Coś jeszcze powinno zostać na dworze. Rozpal w kominku, żebyśmy nie zamarźli.\n ~ Tob'")
        elif argument == "alkierz":
            wypisz("Czy chcesz wynająć pokój, żeby się zregenerować? (5 złota)")
            choice = ""
            while choice not in ["1", "2"]:
                wypisz("1. Tak\n2. Nie", slowo_kolor={"1. Tak": "GREEN", "2. NIE": "RED"})
                choice = input(">")
                os.system("cls")
                if choice == "1":
                    wypisz("Kładziesz się w wynajętym pokoju i odpoczywasz")
                    player.gold -= 5
                    player.hp = player.max_hp
                    player.energy = player.max_energy
                elif choice == "2":
                    wypisz("Może innym razem")
                    continue
        elif argument == "szopa" and currentRoom == "(2,-1)":
            if quests["Drwal"]["active"] and not quests["Drwal"]["completed"]:
                wypisz("Wchodzisz do szopy i znajdujesz tam ciało zaginionego drwala...")
                wypisz("A raczej to co z niego zostało. Próbujesz zbadać ciało, żeby dowiedzieć się co za stwór dopadł tego biedaka")
                if player.blessing == "Oczy przyszłości":
                    wypisz("Dzięki swojemu błogosławieństwu, widzisz nadchodzący atak. Natychmiastowo go unikasz i odracasz się w stronę przeciwnika. Okazuje się, że to żona drwala, a przynajmniej za to się podawał ten potwór. Jego kamuflaż zaczyna się psuć przez co widzisz ciało kobiety, z wydłużonymi kończynami, nienaturalnymi proporcjami i porwaną skórą.")
                    walka(player, dopler)
                else:
                    wypisz("Nagle zostajesz zaatakowany od tyły przez potwora, który podawał się za żonę drwala. Tracisz 10 HP", slowo_kolor={"10 HP": "RED"})
                    player.hp -= 10
                    walka(player, dopler)
                quests["Drwal"]["completed"] = True
                rooms["Targ"]["characters"].remove("smutna kobieta")
                if not rooms["Targ"]["characters"]:
                    del rooms["Targ"]["characters"]
            else:
                wypisz("Stoisz przed zamkniętą szopą. Czujesz smród, ale nie wydaje Ci się to ważne.")
        elif argument == "kominek" and currentRoom == "Hol":
            if "drewno" in player.inventory:
                wypisz("Rozpalasz kominek, dając sobie trochę ciepła. Czujesz się bezpieczniej.")
                player.inventory.remove("drewno")
                rooms[currentRoom]["objects"].remove(argument)
                palisie = True
                quests["Kominek"]["completed"] = True
                wypisz("Słyszysz jakieś dźwięki dochodzące z zewnątrz. To musi być Tob", slowo_bold="Tob", slowo_kolor={"Tob": "YELLOW"})
            else:
                wypisz("Nie masz nic, czym mógłbyś rozpalić kominek.")
        elif argument == "podloga" and currentRoom == "Jadalnia":
            if "miotla" in player.inventory:
                wypisz("Przez kilka godzin zamiatasz paskudne podłogi masywnej sali jadalnej, czujesz się zmęczony, ale też dumny z tego jak to teraz wygląda")
                podlogac = True
                rooms[currentRoom]["objects"].remove(argument)
                if podlogac and stolyust:
                    quests["Jadalnia"]["completed"] = True
                    rooms["Hol"]["description"] = "Jesteś w schludnej jadalni. Wszystko wydaje się być na swoim miejscu. Jedyne co tu nie pasuje to fakt, że nie ma tu nikogo oprócz Ciebie"
            else:
                wypisz("Podłoga jest cała w kurzu, okruchach i resztach jedzenia. Musisz znaleźć coś czym to posprzątasz")
        elif argument == "stoly" and currentRoom == "Jadalnia":
            if quests["Jadalnia"]["active"]:
                wypisz("Spędzasz kilkanaście minut na estetycznym ułożeniu stołów, aż w końcu efekt końcowy jest dla ciebie zadowalający")
                stolyust = True
                rooms[currentRoom]["objects"].remove(argument)
                if podlogac and stolyust:
                    quests["Jadalnia"]["completed"] = True
                    rooms["Hol"]["description"] = "Jesteś w schludnej jadalni. Wszystko wydaje się być na swoim miejscu. Jedyne co tu nie pasuje to fakt, że nie ma tu nikogo oprócz Ciebie"
            else:
                wypisz("Stoły są poustawiane w kątach sali, a niektóre są przewrócone. Ciekawe co się tu wcześniej stało")
        elif argument == "stojaki" and currentRoom == "Zbrojownia":
            if quests["Zbrojownia"]["active"]:
                if "zamowienie" in player.inventory:
                    wypisz("Wykładasz zakupione bronie i zbroje. Zbrojownia w końcu nie jest pusta, ale dalej daleko jej do dobrego stanu")
                    quests["Zbrojownia"]["completed"] = True
                else:
                    wypisz("Musisz najpierw kupić bronie i zbroje u kowala, żeby tu nie było tak pusto")
            else:
                if quests["Zbrojownia"]["completed"]:
                    wypisz("Stojaki prezentują się całkiem nieźle, ale dalej brakuje tu sprzętu.")
                else:
                    wypisz("Stojaki są puste, a zbrojownia wygląda jakby nikt tu nie zaglądał od lat. Nie wygląda to dobrze")
        elif argument == "skrzynia" and currentRoom == "Zbrojownia":
            if quests["Jadalnia"]["completed"]:
                wypisz("Otwierasz w skrzynie a w niej znajdują się 3 bronie. Możesz wybrać tylko jedną ze względu na braki w zaopatrzeniu")
                ch = ""
                while ch not in ["1", "2", "3"]:
                    wypisz("Co wybierasz?")
                    wypisz("1. Prosty miecz dwuręczny (siła)")
                    wypisz("2. Prosta włócznia (zręczność)")
                    wypisz("3. (Inteligencja)")
                    ch = input("> ").strip()
                    if ch == "1":
                        player.inventory.append(prosty_miecz_dwureczny)
                    elif ch == "2":
                        player.inventory.append(prosta_wlocznia)
                    elif ch == "3":
                        player.inventory.append(krotki_miecz)
                tob1 = True
            else:
                wypisz("Próbujesz otworzyć skrzynię, ale nie dajesz rady. Jest zamknięta na klucz. Może Tob coś o tym wie", slowo_bold="Tob", slowo_kolor={"Tob": "YELLOW"})
        elif argument == "regaly" and currentRoom == "Biblioteka":
            wypisz("Przeglądasz regały i znajdujesz kilka interesujących książek. Co chcesz przeczytać?")
            choice = ""
            while choice != "3":
                wypisz("Co chcesz przeczytać? \n1. Bestiariusz \n2. VALANDORSKA KAMPANIA WOJENNA I JEJ KONSEKWENCJE \n3. Powrót")
                choice = input("> ").strip()
                if choice == "1":
                    bestie()
                elif choice == "2":
                    kampania()
                elif choice == "3":
                    os.system("cls")
                    continue
        elif argument == "lozko":
            if palisie:
                wypisz("Kładziesz się na łóżku aby odpocząć. Twoje HP i Energia regenerują się")
                player.hp = player.max_hp
                player.energy = player.max_energy
            else:
                wypisz("Jest zbyt zimno żeby się położyć. Poza tym, nie masz czasu na drzemkę.")
        elif argument == "kukla treningowa" and currentRoom == "Dwor":
            wypisz("Podchodzisz do kukły treningowej i zaczynasz ją atakować, ćwicząc swoje umiejętności bojowe.")
            walka(player, kukla_treningowa)
    elif argument in player.inventory:
        if argument in bronie:
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
        elif argument == "ochraniacze":
            wypisz("Nakładasz ochraniacze, które zwiększają twoją obronę o 10 punktów")
            player.defense += 10
        elif argument == "dziennik":
            dziennik()
        else:
            wypisz(f"Używasz {argument} z ekwipunku, ale nic się nie dzieje.", slowo_kolor={argument: "YELLOW"})

    return palisie, tob1, stolyust, podlogac
