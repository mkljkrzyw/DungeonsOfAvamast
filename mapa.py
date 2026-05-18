directions=["north", "south", "east", "west", "enter", "exit"]
avaiable_directions = []
rooms = {
"Sala Sypialniana": {
    "description": "Jesteś w dużym pomieszczeniu z wysokim sufitem, z niewielkich okien dociera mocne światło spotęgowane śniegiem znajdującym się na dworze. Widzisz wiele twardych łóżek, stolik, oraz leżący na twoim notatnik. Na wschodzie znajdują się drzwi prowadzące do głównego holu",
    "objects": ["lozko","kartka"],
    "east": "Hol"
},
"Hol": {
    "description": "Stoisz w głównym holu, czujesz mróz. Widzisz nierozpalony kominek, zachodnie drzwi prowadzące do sali sypialnianej, połnocne drzwi prowadzące do biblioteki, wschodnie drzwi prowadzące do jadali, oraz wielkie drzwi na południu prowadzące na zewnątrz",
    "objects": ["kominek"],
    "west": "Sala Sypialniana",
    "north": "Biblioteka",
    "east": "Jadalnia",
    "south": "Dwor"
},
"Biblioteka":{
    "description": "Jesteś w bibliotece. Widzisz wiele regałów z książkami, biurko z krzesłem, oraz drzwi prowadzące do głównego holu",
    "objects": ["regaly"],
    "south": "Hol"
},
"Jadalnia": {
    "description": "Jesteś w jadalni. Widzisz długi stół, kilka krzeseł, oraz drzwi prowadzące do głównego holu",
    "objects": ["stol"],
    "west": "Hol"
},
"Dwor": {
    "description": "Jesteś na dziedzińcu. Widzisz fontannę, ławkę, kukłę treningową oraz drzwi prowadzące do korytarza...",
    "objects": ["kukla treningowa"],
    "items_available": ["drewno"],
    #"characters": [""],
    "north": "Hol",
    "exit": "(0,0)"
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
    "objects": ["narzedzia"],
    "south": "Brama Miasteczka"
},
"Karczma": {
    "description": "Jesteś w karczmie. Widzisz kilka stolików, bar, oraz drzwi prowadzące do bramy miasteczka",
    "objects": ["bar"],
    "north": "Brama Miasteczka"
},
"Targ": {
    "description": "Jesteś na targu. Widzisz kilka straganów, smutną kobietę na przy pustym stoisku z resztkami drewna, oraz drzwi prowadzące do bramy miasteczka",
    "objects": ["stragany"],
    "characters": ["smutna kobieta"],
    "west": "Brama Miasteczka"
},
"Ratusz": {
    "description": "Jesteś w ratuszu. Widzisz kilka biurek, oraz drzwi prowadzące do bramy miasteczka",
    "objects": ["biurka"],
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