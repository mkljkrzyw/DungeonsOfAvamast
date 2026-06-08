from interfejs.ui import wypisz
quests={
    #------FABUŁKA-----
    "Kominek":{ #1.Fabularny quest
    "name":"Mróz w wieży",
    "description":"Znajdź drewno i rozpal ogień w kominku",
    "active":True,
    "completed":False,
    "exp":20,

    },
    "Jadalnia":{ #2.Fabularny quest
        "name":"Porządki w Jadalni",
        "description":"Znajdź miotłę i pozamiataj podłogę, ustaw stoły w Sali Jadalnej",
        "active":False,
        "completed":False,
        "exp":20
    },
    "Zbrojownia":{#3.Fabularny quest
        "name":"Uzupełnienie zbrojowni",
        "description":"Zarób pieniądze i kup bronie u kowala w miasteczku",
        "active":False,
        "completed":False,
        "exp":100
    },
    #4. Zbieranie kasy na kupienie wyposażenia. Idziesz do kowala -> daje cene z pizdy, ale jak zrobisz jego questa to obnizy cene
    #Trzeba porobić pare side questów albo farmić sobie kaske
    #grindowy quest
    #potem jak kupisz to idziesz do Toba, a on mówi że ktoś przyjechał i będzie nowa postka
    #-------SIDE QUESTY-----------
    "Drwal":{"name":"Zaginiony drwal", #dopler
    "description":"Pomóż smutnej kobiecie odnaleźć jej męża, który zaginął podczas pracy w lesie.",
    "active": False,
    "completed": False,
    "exp": 80,
    "gold":10,
    },

    "Kowal":{
    "description":"",
    "active": False,
    "completed": False,
    "exp": 10,
    }

    #--------questline Varina---------
    #kupienie piwa w barze
    #uratowanie kotow

    #--------questline Ignotusa----------
    #questline ignotusa
    #jakies lizanie dupy ignotusowi
    #gamblowanie i przegrana
}
def dziennik():
    wypisz("Dziennik zadań:")
    for quest in quests:
        if quests[quest]["active"] and not quests[quest]["completed"]:
            wypisz(f"- {quests[quest]['name']}: {quests[quest]['description']}")
    wypisz("--------------")
    for quest in quests:
        if quests[quest]["completed"]:
            wypisz(f"- {quests[quest]['name']}: Zakończone")

