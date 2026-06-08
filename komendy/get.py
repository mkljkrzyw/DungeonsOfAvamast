from interfejs.ui import wypisz


def handle_get(player, currentRoom, rooms, argument):
    if not argument:
        wypisz("Podaj obiekt do użycia, np. 'get piwo'.", slowo_kolor={"use": "YELLOW"})
    elif argument == "wielki mlot":
        if player.blessing == "Manipulacja ciężarem":
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
