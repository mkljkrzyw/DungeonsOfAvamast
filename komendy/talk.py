import os

from interfejs.ui import wypisz


def handle_talk(player, currentRoom, rooms, quests, argument, tob_location, tob1, tob2, kowal1):
    if not argument:
        wypisz("Podaj imię postaci, z którą chcesz porozmawiać, np. 'talk Tob'.", slowo_kolor={"talk": "GREEN"})
    elif "characters" in rooms[currentRoom] and argument in [char.lower() for char in rooms[currentRoom]["characters"]]:
        if argument == "tob" and currentRoom == "Dwor" and tob_location == "dwor":
            wypisz("Tob: Hej, cieszę się, że się obudziłeś. Przyszedłem z nową dostawą drewna. Trochę mi to zajęło, ponieważ zaginął lokalny drwal, ale nie miałem czasu tego zbadać. W wolnym czasie idź do wioski, która znajduje się na północnym wschodzie i zobacz czy to coś poważnego. Idę do środka się ogrzać. Porozmawiamy później.", kolor="LIGHT_CYAN", slowo_bold="Tob")
            rooms["Dwor"]["characters"].remove("Tob")
            if not rooms["Dwor"]["characters"]:
                del rooms["Dwor"]["characters"]
            rooms["Hol"].setdefault("characters", [])
            if "Tob" not in rooms["Hol"]["characters"]:
                rooms["Hol"]["characters"].append("Tob")
            tob_location = "hol"
        elif argument == "tob" and currentRoom == "Hol" and tob_location == "hol":
            if tob1:
                wypisz("Tob: Widziałeś już stan naszej zbrojowni. Oboje wiemy że nie jest ciekawie. Masz tutaj 100 monet. Tylko tyle mogę na to przeznaczyć, ale to i tak nie wystarczy. Musisz też się dorzucić. Jak nie masz nic przy sobie to zapytaj mieszkańców miasteczka o jakieś zlecenia. Wróć do mnie jak kupisz bronie u kowala i odłożysz je do zbrojowni")
                quests["Zbrojownia"]["active"] = True
                player.gold += 100
            elif quests["Zbrojownia"]["completed"]:
                wypisz("Świetna robota, jak Ciebie nie było przyjechał do nas gość. To Ketan, idź się z nim przywitać. Pewnie jest teraz na dworze")
                if "Ketan" not in rooms["dwor"]["characters"]:
                    rooms["dwor"]["characters"].append("Ketan")
            elif quests["Jadalnia"]["completed"]:
                wypisz("Tob: Świetna robota, przy okazji chodź za mną, to otworzę ci skrzynię w zbrojowni. Kompletnie mi to wyleciało z głowy przez ten natłok pracy", kolor="LIGHT_CYAN", slowo_bold="Tob")
                currentRoom = "Zbrojownia"
            elif quests["Jadalnia"]["active"]:
                wypisz("Tob: Miałeś posprzątać jadalnię. Nie zawracaj mi głowy, dopóki tego nie zrobisz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
            else:
                wypisz("Tob: Musimy zająć szykowaniem się wieży. Nie wiem, co się dzieje, ale coś jest nie tak, skoro nas tu wysłali. Podobno szykuje się jakaś duża bitwa. Zacznij od posprzątania jadalni. Muszę jeszcze trochę odpocząć, więc wróć do mnie jak skończysz.", kolor="LIGHT_CYAN", slowo_bold="Tob")
                quests["Jadalnia"]["active"] = True
        elif argument == "kowal":
            if kowal1:
                if quests["Kowal"]["active"]:
                    wypisz("Kowal: Pogadamy jak skończysz robić to o co cię poprosiłem", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                elif not quests["Kowal"]["active"]:
                    if not quests["Zbrojownia"]["active"]:
                        print("Xd")
                    elif player.gold >= 500:
                        wypisz("Całkiem szybko Ci poszło. O to twoje zamówienie")
                        player.gold -= 500
                        player.inventory.append("zamowienie")
                    else:
                        wypisz("Kowal: Zmieniełeś zdanie?", kolor="LIGHT_CYAN", slowo_bold="Kowal:")
                        choice = ""
                        while choice not in ["1", "2"]:
                            os.system("cls")
                            wypisz("1. Tak, jednak Ci pomogę \n2. Nie", slowo_bold="1.;2.", slowo_kolor={"1.": "GREEN", "2.": "RED"})
                            choice = input("> ").strip()
                            if choice == "1":
                                wypisz("Kowal: Bardzo dobrze, nwcoswymyslexd", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                                quests["Kowal"]["active"] = True
                            elif choice == "2":
                                wypisz("Kowal: No cóż, to Twoja strata. Wracaj jak uzbierasz 500 złota, no chyba że zmienisz zdanie", kolor="LIGHT_CYAN", slowo_bold="Kowal")
            if quests["Zbrojownia"]["active"] and not kowal1:
                wypisz(f"{player.name}: Potrzebuje różnych broni i zbroi. Oto lista")
                wypisz("Kowal: Po co ci takie duże zamówienie młody. No nic, to nie moja sprawa. Przyszkowanie tego wszystkiego trochę zajmie, możesz w tym czasie mi pomóc to odrazu dostaniesz zniżke. Normalnie taka oferta kosztowałaby 500 złota, ale jak zrobisz o co Cię proszę to dam Ci to wszystko za 300. Jaka decyzja?", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                choice = ""
                while choice not in ["1", "2"]:
                    os.system("cls")
                    wypisz("1. Pomogę Ci \n2. Nie mam czasu", slowo_bold="1.;2.", slowo_kolor={"1.": "GREEN", "2.": "RED"})
                    choice = input("> ").strip()
                    if choice == "1":
                        wypisz("Kowal: Bardzo dobrze, nwcoswymyslexd", kolor="LIGHT_CYAN", slowo_bold="Kowal")
                        quests["Kowal"]["active"] = True
                    elif choice == "2":
                        wypisz("Kowal: No cóż, to Twoja strata. Wracaj jak uzbierasz 500 złota, no chyba że zmienisz zdanie", kolor="LIGHT_CYAN", slowo_bold="Kowal")
            kowal1 = True
        elif argument == "smutna kobieta" and currentRoom == "Targ":
            wypisz("Smutna kobieta: Witaj. Jeżeli przyszedłeś tu po drewno to muszę Cię zasmucić. Zamykamy biznes. Mój mąź zaginął, a to on dostarczał mi drewno. Nie mam z nim żadnego kontaktu od tygodnia. Nikt nie chce mi pomóc, sprawdzić co się stało, a nie mogę pójść sama ponieważ w pobliżu krążą bandyci. Proszę pójdź ze mną do naszego tartaku, który znajduje się na południe od miasta", kolor="LIGHT_CYAN", slowo_bold="Smutna kobieta")
            quests["Drwal"]["active"] = True
        else:
            wypisz(f"Nie rozmawiać z {argument}.", slowo_kolor={argument: "RED"})
    else:
        wypisz(f"Nie ma tutaj postaci o imieniu {argument}.", slowo_kolor={argument: "RED"})

    return tob_location, tob1, tob2, kowal1
