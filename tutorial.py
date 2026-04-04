import os
from characters import Player
os.system("cls")
def help():
    print('''
Dungeons of Avamast
=================
Commands:
    go [direction]
    get [item]
    use [item]
    inventory 
    stats
    help
''')



def tutorial(player):
    currentRoom = "Sypialnia"
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
        "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę oraz drzwi prowadzące do korytarza.",
        "south": "Korytarz"
    }
    }
    
    print("Budzisz się w swoim pokoju, w dobrze znanej twierdzy Ezelthorn. Coś jednak wydaje się nie tak. Wszystko jest ciche, a ty nie pamiętasz, co się stało. Musisz znaleźć sposób, by wydostać się z tej sytuacji.")
    help()
    while True:
        print("\n" + rooms[currentRoom]["description"])
        turn = input("> ")
        os.system("cls")
        turn = turn.split(" ",1)
        if turn[0]=="use":
            if "objects" in rooms[currentRoom] and turn[1] in rooms[currentRoom]["objects"]:
                if turn[1] == "skrzynia":
                    print("Otwierasz skrzynię i znajdujesz piwo. Dodajesz je do swojego ekwipunku.")
                    player.inventory.append(rooms[currentRoom]["items_available"])
                    rooms[currentRoom]["items_available"] = None
                    rooms[currentRoom]["objects"].remove(turn[1])
                elif turn[1] == "kartka":
                    print("Aby uzyskać pomoc odnośnie komend, wpisz 'help'.")
                    rooms[currentRoom]["objects"].remove(turn[1])
            else:
                print(f"Nie ma tutaj {turn[1]}.")
        elif turn[0]=="go":
            if turn[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][turn[1]]
                if currentRoom == "dziedziniec":
                    print("Nagle atakuje cię Rapax. Jego ostre szpony przebijają twoją skórę, a jego pazury tną głęboko. Zanim zdążysz zareagować czujesz nagły ból, a potem wszystko staje się białe.")
            else:
                print("Nie możesz iść w tym kierunku.")
        elif turn[0]=="inventory":
            print("Ekwipunek: " + str(player.inventory))
        elif turn[0]=="stats":
            player.show_stats()
        elif turn[0]=="help":
            help()