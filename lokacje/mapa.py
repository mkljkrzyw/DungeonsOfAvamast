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
"Sala Sypialniana": {
    "description": "Jesteś w dużym pomieszczeniu z wysokim sufitem, z niewielkich okien dociera mocne światło spotęgowane śniegiem znajdującym się na dworze. Widzisz wiele twardych łóżek, stolik, oraz leżący na nim dziennik. Na wschodzie znajdują się drzwi prowadzące do głównego holu",
    "objects": ["lozko","kartka"], #lozko - heal, kartka - informacja o quescie 
    "items_available": ["dziennik"], #wypisane questy
    "east": "Hol"
},
"Hol": {
    "description": "Stoisz w głównym holu, czujesz mróz. Widzisz nierozpalony kominek, zachodnie drzwi prowadzące do sali sypialnianej, połnocne drzwi prowadzące do biblioteki, wschodnie drzwi prowadzące do jadali, oraz wielkie drzwi na południu prowadzące na zewnątrz",
    "objects": ["kominek"],#pierwszy quest
    "west": "Sala Sypialniana",
    "north": "Biblioteka",
    "east": "Jadalnia",
    "south": "Dwor"
},
"Biblioteka":{
    "description": "Jesteś w bibliotece. Widzisz wiele regałów z książkami, biurko z krzesłem, oraz drzwi prowadzące do głównego holu",
    "objects": ["regaly"],#ksiazki
    "items_available":["miotla","mapa"],#do questa w jadalni
    "south": "Hol"
},
"Jadalnia": {
    "description": "Jesteś w jadalni. Widzisz długi stół, kilka krzeseł, oraz drzwi prowadzące do głównego holu",
    "objects": ["stoly","podloga"],#quest z miotłą
    "west": "Hol"
},
"Dwor": {
    "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę, kukłę treningową oraz drzwi prowadzące do korytarza...",
    "objects": ["kukla treningowa"],#classic
    "items_available": ["drewno"],#pierwszy quest
    #"characters": [""],
    "east":"Zbrojownia",
    "north": "Hol",
    "exit": "(0,0)"
},
"Zbrojownia":{
    "description":"Jesteś w przestronnej zbrojowni. Niestety oprócz jedną zbroją i skrzynią nie ma tu żadnego sprzętu. Domyślasz się, że tym pewnie też będziesz musiał się zająć. Na zachodzie znajdują się drzwi prowadzące na zewnątrz",
    "objects":["skrzynia","stojaki"],#po jadalni darmowa bronka
    "items_avaiable":["ochraniacze","wielki mlot"], #ochraniacze - wiekszy def; mlot - dla manipulacji ciezarem
    "west":"Dwor"
},
#----Miasteczko----
"Brama Miasteczka": {
    "description": "Jesteś przy bramie spokojnego miasteczka, które wydaje się opustoszałe. Ludzie mieszkający tutaj pewnie mają tutaj już i tak dużo zmartwień, a to nic w porównaniu do wydarzeń które mogą się niedługo tutaj wydarzyć. Słyszysz rzadkie rozmowy, posępne rozmowy kupców. Na północy widzisz sklep kowala, na południu karczmę, na wschodzie opustoszały targ, a na zachodzie duży dom, który wygląda na ratusz.",
    "north": "Sklep Kowala",
    "south": "Karczma",
    "east": "Targ",
    "west": "Ratusz",
    "exit": "(2,2)"
},
"Sklep Kowala": {
    "description": "Jesteś w sklepie kowala. Widzisz kilka narzędzi, kuźnię, oraz drzwi prowadzące do bramy miasteczka",
    #"objects": ["narzedzia"],
    "characters":["Kowal"],
    "south": "Brama Miasteczka"
},
"Karczma": {
    "description": "Jesteś w karczmie. Widzisz kilka stolików, bar, oraz drzwi prowadzące do bramy miasteczka",
    "objects": ["alkierz"],
    "characters":["Darn"],
    "north": "Brama Miasteczka"
},
"Targ": {
    "description": "Jesteś na targu. Widzisz kilka straganów, smutną kobietę na przy pustym stoisku z resztkami drewna, oraz drzwi prowadzące do bramy miasteczka",
    "objects": ["stragany"], 
    "characters": ["smutna kobieta","Farmer","Szarlatan"], #quest z drwalem
    "west": "Brama Miasteczka"
},
"Ratusz": {
    "description": "Jesteś w ratuszu. Widzisz kilka biurek, oraz drzwi prowadzące do bramy miasteczka",
    #"objects": ["biurka"],
    "east": "Brama Miasteczka"
},
#----MAPA ŚWIATA----
"(0,0)": {
    "description": "Stoisz przed ogromną, ponurą wieżą, którą widać stąd w całości. Na samą myśl o tym po co tu jesteś, przechodzi cię dreszcz, a pogoda na dworze jedynie potęguje to uczucie",
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
},
"(2,-1)": {
    "description": "Widzisz mały tartak, pośrodku drzew, czujesz mocny smród zgnilizny dochodzący z szopy.",
    "objects": ["szopa"], #quest z drwalem
},
"(-3,3)":{
    "description":"Wszedłeś w teren burzy, masz ograniczone pole widzenia i czujesz się słabo. Przytłacza Cię potęga burzy i wiesz że musisz uciekać jeśli chcesz przeżyć"
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

punkty_kluczowe = {
    "(0,0)": "Wieża",
    "(2,2)": "Miasteczko",
    "(2,-1)": "Tartak",
}
strefa_potworow = {
    "(-3,2)","(-3,1)","(-3,0)","(-3,-1)","(-3,-2)","(-3,-3)","(-2,3)","(-2,2)","(-2,1)","(-2,0)","(-2,-1)","(-2,-2)","(-2,-3)","(-1,-2)","(-1,-3)","(0,-2)","(1,-2)","(1,-3)"
}
strefa_bandytow = {
    "(-1,3)","(0,3)","(2,3)","(3,3)","(3,2)","(3,1)","(3,0)","(3,-1)","(0,2)","(1,2)","(2,1)","(2,0)"
}
for i in strefa_potworow:
    rooms[i]["description"] = f"Przemierzasz zaśnieżone pustkowia. Pogoda wokół ciebie jest coraz mroczniejsza. Wyczuwasz obecność burzy niedaleko Ciebie. Czujesz, że na tym terenie mogą czaić się potwory."
for i in strefa_bandytow:
    rooms[i]["description"] = f"Przemierzasz zaśnieżone pustkowia. Widać nieliczne ślady stóp. Czujesz, że powinieneś zachować ostrożność."
# Tłumaczenie lokacji wewnętrznych na pozycję na świecie
pozycja_na_swiecie = {
    "Sala Sypialniana": (0,0), "Hol": (0,0), "Biblioteka": (0,0), 
    "Jadalnia": (0,0), "Dwor": (0,0), "Zbrojownia": (0,0),
    "Brama Miasteczka": (2,2), "Sklep Kowala": (2,2), 
    "Karczma": (2,2), "Targ": (2,2), "Ratusz": (2,2)
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


def uzyj_mape(obecny_pokoj):
    if obecny_pokoj in pozycja_na_swiecie:
        gracz_x, gracz_y = pozycja_na_swiecie[obecny_pokoj]
    else:
        try:
            czysty_tekst = obecny_pokoj.replace("(", "").replace(")", "")
            gracz_x, gracz_y = map(int, czysty_tekst.split(","))
        except:
            print("Nie możesz tutaj użyć mapy.")
            return

    print("\n" + "=================================== ROZWIJASZ MAPĘ ŚWIATA ===================================".center(105))
    print()

    # Rysujemy macierz 7x7 (Y od 3 do -3; X od -3 do 3)
    for y in range(3, -4, -1):
        linia_mapy = ""
        for x in range(-3, 4):
            koordynaty_kafelka = f"({x},{y})"
            
            if x == gracz_x and y == gracz_y:
                wyglad_kafelka = "[* TY *]"
            elif koordynaty_kafelka in punkty_kluczowe:
                wyglad_kafelka = f"[{punkty_kluczowe[koordynaty_kafelka]}]"
            else:
                wyglad_kafelka = f"[ {x},{y} ]"
                
            linia_mapy += wyglad_kafelka.center(15)
            
        print(linia_mapy)
        print() 

    print("=" * 105 + "\n")