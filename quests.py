from ui import wypisz
quests={
    "Kominek":{
    "name":"Mróz w wieży",
    "description":"Znajdź drewno i rozpal ogień w kominku",
    "active":True,
    "completed":False,
    "exp":20,

    },
    "Jadalnia":{
        "name":"Porządki w Jadalni",
        "description":"Znajdź miotłę i pozamiataj podłogę, ustaw stoły w Sali Jadalnej",
        "active":False,
        "completed":False,
        "exp":20
    },
    "Zbrojownia":{
        "name":"Uzupełnienie zbrojowni",
        "description":"Zarób pieniądze i kup bronie u kowala w miasteczku",
        "active":False,
        "completed":False,
        "exp":100
    },
    "Drwal":{"name":"Zaginiony drwal",
    "description":"Pomóż smutnej kobiecie odnaleźć jej męża, który zaginął podczas pracy w lesie.",
    "active": False,
    "completed": False,
    "exp": 80,
    "items": ""}
}
def dziennik():
    wypisz("Dziennik zadań:")
    for quest in quests:
        if quests[quest]["active"] and not quests[quest]["completed"]:
            wypisz(f"- {quests[quest]["name"]}: {quests[quest]["description"]}")
    wypisz("--------------")
    for quest in quests:
        if quests[quest]["completed"]:
            wypisz(f"- {quests[quest]['name']}: Zakończone")