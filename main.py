import os
from books import bestie, kampania
from ui import wypisz, help, bestiariusz
from monsters import dopler, kukla_treningowa, rapax
from fights import walka
from characters import Player
from weapons import *
from lokacjewiz import *
from mapa import *
from quests import *
def main(player):
    player.hp=player.max_hp
    player.inventory=[""]
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
    currentRoom="Sala Sypialniana"
    os.system("cls")
    wypisz("Gwałtownie budzisz się na niewygodnym materacu w jasnym pomieszczeniu. Jesteś w południowej wieży w Thalindorze. Czujesz jedynie mróz i wilgoć. Widzisz przed sobą drzwi, które prowadzą na korytarz. Sen który miałeś wydawał się tak realny, że nie jesteś jeszcze pewien, czy to był tylko sen. Nie pamiętasz z niego praktycznie nic, ale również nie pamiętasz po co tutaj jesteś")
    while True:
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
        turn = input("> ").strip()
        while turn=="":
            turn = input()
        os.system("cls")
        turn = turn.split(" ", 1)
        komenda = turn[0].lower() if turn and turn[0] else ""
        argument = turn[1].strip().lower() if len(turn) > 1 else ""
#---------------------------KOMENDA USE---------------------------
##################################################################
        if komenda == "use":
            bronie = {
                "prosta wlocznia": prosta_wlocznia,
                "prosty miecz dwureczny":prosty_miecz_dwureczny
            }
            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'use skrzynia'.", slowo_kolor={"use": "GREEN"})
            elif "objects" in rooms[currentRoom] and argument in rooms[currentRoom]["objects"]:
                if argument == "kartka" and currentRoom == "Sala Sypialniana":
                    wypisz("Na kartce napisane jest 'Wyszedłem po drzewo. Coś jeszcze powinno zostać na dworze. Rozpal w kominku, żebyśmy nie zamarźli.\n ~ Tob'")
                elif argument=="alkierz":
                    wypisz("Czy chcesz wynająć pokój, żeby się zregenerować? (5 złota)")
                    choice=""
                    while choice not in["1","2"]:
                        
                        wypisz("1. Tak\n2. Nie",slowo_kolor={"1. Tak":"GREEN","2. NIE":"RED"})
                        choice=input(">")
                        os.system("cls")
                        if choice==1:
                            wypisz("Kładziesz się w wynajętym pokoju i odpoczywasz")
                            player.gold-=5
                            player.hp=player.max_hp
                            player.energy=player.max_energy
                        elif choice==2:
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
                        palisie=True
                        quests["Kominek"]["completed"]=True
                        wypisz("Słyszysz jakieś dźwięki dochodzące z zewnątrz. To musi być Tob", slowo_bold="Tob", slowo_kolor={"Tob": "YELLOW"})
                    else:
                        wypisz("Nie masz nic, czym mógłbyś rozpalić kominek.")
                elif argument=="podloga" and currentRoom=="Jadalnia":
                    if "miotla" in player.inventory:
                        wypisz("Przez kilka godzin zamiatasz paskudne podłogi masywnej sali jadalnej, czujesz się zmęczony, ale też dumny z tego jak to teraz wygląda")
                        podlogac=True
                        rooms[currentRoom]["objects"].remove(argument)
                        if podlogac==True and stolyust==True:
                            quests["Jadalnia"]["completed"]=True
                            rooms["Hol"]["description"]="Jesteś w schludnej jadalni. Wszystko wydaje się być na swoim miejscu. Jedyne co tu nie pasuje to fakt, że nie ma tu nikogo oprócz Ciebie"
                    else:
                        wypisz("Podłoga jest cała w kurzu, okruchach i resztach jedzenia. Musisz znaleźć coś czym to posprzątasz")
                elif argument == "stoly"and currentRoom=="Jadalnia":
                    if quests["Jadalnia"]["active"]==True:
                        wypisz("Spędzasz kilkanaście minut na estetycznym ułożeniu stołów, aż w końcu efekt końcowy jest dla ciebie zadowalający")
                        stolyust=True
                        rooms[currentRoom]["objects"].remove(argument)
                        if podlogac==True and stolyust==True:
                            quests["Jadalnia"]["completed"]=True
                            rooms["Hol"]["description"]="Jesteś w schludnej jadalni. Wszystko wydaje się być na swoim miejscu. Jedyne co tu nie pasuje to fakt, że nie ma tu nikogo oprócz Ciebie"
                    else:
                        wypisz("Stoły są poustawiane w kątach sali, a niektóre są przewrócone. Ciekawe co się tu wcześniej stało")
                elif argument=="stojaki" and currentRoom == "Zbrojownia":
                    if quests["Zbrojownia"]["active"]==True:
                        if "zamowienie" in player.inventory:
                            wypisz("Wykładasz zakupione bronie i zbroje. Zbrojownia w końcu nie jest pusta, ale dalej daleko jej do dobrego stanu")
                            quests["Zbrojownia"]["completed"]=True
                        else:
                            wypisz("Musisz najpierw kupić bronie i zbroje u kowala, żeby tu nie było tak pusto")
                    else:
                        if quests["Zbrojownia"]["completed"]==True:
                            wypisz("Stojaki prezentują się całkiem nieźle, ale dalej brakuje tu sprzętu.")
                        else:
                            wypisz("Stojaki są puste, a zbrojownia wygląda jakby nikt tu nie zaglądał od lat. Nie wygląda to dobrze")
                elif argument == "skrzynia"and currentRoom == "Zbrojownia":
                    if quests["Jadalnia"]["completed"]==True:
                        wypisz("Otwierasz w skrzynie a w niej znajdują się 3 bronie. Możesz wybrać tylko jedną ze względu na braki w zaopatrzeniu")
                        ch=""
                        while ch not in["1","2","3"]:
                            wypisz("Co wybierasz?")
                            wypisz("1. Prosty miecz dwuręczny (siła)")
                            wypisz("2. Prosta włócznia (zręczność)")
                            wypisz("3. (Inteligencja)")
                            ch = input("> ").strip()
                            if ch==1:
                                player.inventory.append(prosty_miecz_dwureczny)
                            elif ch==2:
                                player.inventory.append(prosta_wlocznia)
                            elif ch==3:
                                player.inventory.append(krotki_miecz)
                        tob1=True             
                    else:
                        wypisz("Próbujesz otworzyć skrzynię, ale nie dajesz rady. Jest zamknięta na klucz. Może Tob coś o tym wie", slowo_bold="Tob", slowo_kolor={"Tob": "YELLOW"})
                elif argument == "regaly" and currentRoom == "Biblioteka":
                    wypisz("Przeglądasz regały i znajdujesz kilka interesujących książek. Co chcesz przeczytać?")
                    choice=""
                    while choice!="3":
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
                    if palisie:
                        wypisz("Kładziesz się na łóżku aby odpocząć. Twoje HP i Energia regenerują się")
                        player.hp=player.max_hp
                        player.energy=player.max_energy
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
                elif argument=="ochraniacze":
                    wypisz("Nakładasz ochraniacze, które zwiększają twoją obronę o 10 punktów")
                    player.defense += 10
                elif argument == "dziennik":
                        dziennik()
                else:
                    wypisz(f"Używasz {argument} z ekwipunku, ale nic się nie dzieje.", slowo_kolor={argument: "YELLOW"})
#---------------------------KOMENDA GO---------------------------
##################################################################
        elif komenda == "go":
            if not argument:
                wypisz("Nieznany kierunek.", kolor="RED")
            elif argument in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][argument]
            else:
                wypisz("Nie możesz iść w tym kierunku.", kolor="RED")
#---------------------------KOMENDA GET---------------------------
##################################################################
        elif komenda == "get":
            if not argument:
                wypisz("Podaj obiekt do użycia, np. 'get piwo'.", slowo_kolor={"use": "YELLOW"})
            elif argument=="wielki mlot":
                if player.blessing=="Manipulacja ciężarem":
                    wypisz(f"Podnosisz {argument} i dodajesz go do swojego ekwipunku.", slowo_kolor={argument: "YELLOW"})
                    player.inventory.append(argument)
                    rooms[currentRoom]["items_available"].remove(argument)
                else:
                    wypisz("Młot jest dla Ciebie za ciężki")
            elif argument in rooms[currentRoom].get("items_available", []):
                wypisz(f"Podnosisz {argument} i dodajesz go do swojego ekwipunku.", slowo_kolor={argument: "YELLOW"})
                player.inventory.append(argument)
                rooms[currentRoom]["items_available"].remove(argument)
            else:
                wypisz(f"Nie ma tutaj, ani w twoim ekwipunku {argument}.", slowo_kolor={argument: "RED"})
#---------------------------KOMENDA TALK---------------------------
##################################################################
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
                    if tob1:
                        wypisz("Tob: Widziałeś już stan naszej zbrojowni. Oboje wiemy że nie jest ciekawie. Masz tutaj 100 monet. Tylko tyle mogę na to przeznaczyć, ale to i tak nie wystarczy. Musisz też się dorzucić. Jak nie masz nic przy sobie to zapytaj mieszkańców miasteczka o jakieś zlecenia. Wróć do mnie jak kupisz bronie u kowala i odłożysz je do zbrojowni")
                        quests["Zbrojownia"]["active"]=True
                        player.gold += 100
                    elif quests["Zbrojownia"]["completed"]==True:
                        wypisz("Świetna robota, jak Ciebie nie było przyjechał do nas gość. To Ketan, idź się z nim przywitać. Pewnie jest teraz na dworze")
                        if "Ketan" not in rooms["dwor"]["characters"]:
                            rooms["dwor"]["characters"].append("Ketan")
                    elif quests["Jadalnia"]["completed"]==True:
                        wypisz("Tob: Świetna robota, przy okazji masz klucz do skrzyni w zbrojowni. Zapomniałem go odłożyć na miejsce. Wybierz sobie coś co ci odpowiada i wróć tutaj", kolor="LIGHT_CYAN", slowo_bold="Tob")
                    elif quests["Jadalnia"]["active"]==True:
                        wypisz("Tob: Miałeś posprzątać jadalnię. Nie zawracaj mi głowy, dopóki tego nie zrobisz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                    else:
                        wypisz("Tob: Musimy zająć szykowaniem się wieży. Nie wiem, co się dzieje, ale coś jest nie tak, skoro nas tu wysłali. Podobno szykuje się jakaś duża bitwa. Zacznij od posprzątania jadalni. Muszę jeszcze trochę odpocząć, więc wróć do mnie jak skończysz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                        quests["Jadalnia"]["active"]=True
                elif argument == "kowal":
                    if kowal1:
                        if quests["Kowal"]["active"]==True:
                            wypisz("Kowal: Pogadamy jak skończysz robić to o co cię poprosiłem", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                        elif quests["Kowal"]["active"]==False:
                            if quests["Zbrojownia"]["active"]==False:
                                #tutaj po skonczeniu questa
                                print("Xd")
                            elif player.gold>=500:
                                wypisz("Całkiem szybko Ci poszło. O to twoje zamówienie")
                                player.gold-=500
                                player.inventory.append("zamowienie")
                            else:
                                wypisz("Kowal: Zmieniełeś zdanie?", kolor="LIGHT_CYAN", slowo_bold="Kowal:")
                                choice=""
                                while choice not in ["1","2"]:
                                    os.system("cls")
                                    wypisz("1. Tak, jednak Ci pomogę \n2. Nie", slowo_bold="1.;2.", slowo_kolor={"1.": "GREEN", "2.":"RED"})
                                    choice = input("> ").strip()
                                    if choice == "1":
                                        wypisz("Kowal: Bardzo dobrze, nwcoswymyslexd", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                                        quests["Kowal"]["active"]=True
                                    elif choice == "2":
                                        wypisz("Kowal: No cóż, to Twoja strata. Wracaj jak uzbierasz 500 złota, no chyba że zmienisz zdanie", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                    if quests["Zbrojownia"]["active"]==True and kowal1==False:
                        wypisz(f"{player.name}: Potrzebuje różnych broni i zbroi. Oto lista")
                        wypisz("Kowal: Po co ci takie duże zamówienie młody. No nic, to nie moja sprawa. Przyszkowanie tego wszystkiego trochę zajmie, możesz w tym czasie mi pomóc to odrazu dostaniesz zniżke. Normalnie taka oferta kosztowałaby 500 złota, ale jak zrobisz o co Cię proszę to dam Ci to wszystko za 300. Jaka decyzja?", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                        choice=""
                        while choice not in ["1","2"]:
                            os.system("cls")
                            wypisz("1. Pomogę Ci \n2. Nie mam czasu", slowo_bold="1.;2.", slowo_kolor={"1.": "GREEN", "2.":"RED"})
                            choice = input("> ").strip()
                            if choice == "1":
                                wypisz("Kowal: Bardzo dobrze, nwcoswymyslexd", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                                quests["Kowal"]["active"]=True
                            elif choice == "2":
                                wypisz("Kowal: No cóż, to Twoja strata. Wracaj jak uzbierasz 500 złota, no chyba że zmienisz zdanie", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                    kowal1=True
                

                elif argument == "smutna kobieta" and currentRoom == "Targ":
                    wypisz("Smutna kobieta: Witaj. Jeżeli przyszedłeś tu po drewno to muszę Cię zasmucić. Zamykamy biznes. Mój mąź zaginął, a to on dostarczał mi drewno. Nie mam z nim żadnego kontaktu od tygodnia. Nikt nie chce mi pomóc, sprawdzić co się stało, a nie mogę pójść sama ponieważ w pobliżu krążą bandyci. Proszę pójdź ze mną do naszego tartaku, który znajduje się na południe od miasta",kolor="LIGHT_CYAN", slowo_bold="Smutna kobieta")
                    quests["Drwal"]["active"] = True
                else:
                    wypisz(f"Nie rozmawiać z {argument}.", slowo_kolor={argument: "RED"})
            else:
                wypisz(f"Nie ma tutaj postaci o imieniu {argument}.", slowo_kolor={argument: "RED"})
#---------------------------POZOSTAŁE---------------------------
##################################################################
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