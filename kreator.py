import os

from characters import Player
from ui import wypisz

STATS_PRESETY = {
    "1": (15, 5, 5),
    "2": (5, 15, 5),
    "3": (5, 5, 15),
}

BLOGOSLAWIENSTWA = {
    "1": "Oczy przyszłości",
    "2": "Manipulacja krwią",
    "3": "Manipulacja ciężarem",
}


def wyczysc_ekran():
    os.system("cls")


def zapytaj_tak_nie(komunikat, niepoprawny="Proszę wpisać 'tak' lub 'nie'.", **wypisz_kwargs):
    while True:
        wyczysc_ekran()
        wypisz(komunikat, **wypisz_kwargs)
        odpowiedz = input("> ").strip().lower()
        if odpowiedz in ["tak", "nie"]:
            return odpowiedz
        wypisz(niepoprawny)


def wybierz_imie_gracza():
    while True:
        wypisz("Podaj imię swojego bohatera: (Podstawowo imie to Grol)", kolor="CYAN")
        player_name = input("> ").strip()
        if player_name == "":
            player_name = "Grol"
        wyczysc_ekran()

        potwierdzenie = zapytaj_tak_nie(

            f"Twoje imię to {player_name}. Czy chcesz je zachować? (tak/nie)", 
            slowo_bold="tak/nie;{player_name}",
            slowo_kolor={"tak": "GREEN", "nie": "RED"}
        )
        wyczysc_ekran()

        if potwierdzenie == "tak":
            return player_name


def wybierz_statystyki():
    while True:
        wypisz("Wybierz swoją główną cechę:", kolor="CYAN")
        wypisz("1. Siła", slowo_bold="1.")
        wypisz("2. Zręczność", slowo_bold="2.")
        wypisz("3. Inteligencja", slowo_bold="3.")
        wypisz("inne - zrównoważony rozkład punktów")

        choice = input("> ").strip()
        strength, dexterity, intelligence = STATS_PRESETY.get(choice, (9, 8, 8))
        wyczysc_ekran()

        potwierdzenie = zapytaj_tak_nie(
            (
                "Twoje statystyki to - "
                f"Siła: {strength}, Zręczność: {dexterity}, Inteligencja: {intelligence}. "
                "Czy chcesz je zachować? (tak/nie)"
            ),
            slowo_bold="tak/nie;{dexterity};{intelligence};{strength}",
            slowo_kolor={"tak": "GREEN", "nie": "RED"}
        )
        wyczysc_ekran()

        if potwierdzenie == "tak":
            return strength, dexterity, intelligence


def wybierz_blogoslawienstwo():
    while True:
        wypisz("Teraz wybierz swoje błogosławieństwo:", opoznienie=0.01, kolor="CYAN", styl="BOLD")
        wypisz(
            "1. Oczy przyszłości (pozwala zobaczyć ukryte pułapki, skarby i przyszłe ruchy przeciwników)",
            opoznienie=0.01,
            slowo_bold="1.",
        )
        wypisz(
            "2. Manipulacja krwią (pozwala tworzyć bronie z krwi, zwiększa obrażenia i szybkość ataku, pozwala się leczyć)",
            opoznienie=0.01,
            slowo_bold="2.",
        )
        wypisz(
            "3. Manipulacja ciężarem (Pozwala nosić najcięższe zbroje i broń, zwiększa obronę i obrażenia po znalezieniu odpowiedniego ekwipunku)",
            opoznienie=0.01,
            slowo_bold="3.",
        )
        wypisz("inne - brak błogosławieństwa", opoznienie=0.01, slowo_bold="inne")

        wybor = input("> ").strip()
        blessing = BLOGOSLAWIENSTWA.get(wybor, "Brak")
        wyczysc_ekran()

        potwierdzenie = zapytaj_tak_nie(
            f"Twoje błogosławieństwo to {blessing}. Czy chcesz je zachować? (tak/nie)",
            slowo_bold="tak/nie;{blessing}",
            slowo_kolor={"tak": "GREEN", "nie": "RED"}
        )
        wyczysc_ekran()

        if potwierdzenie == "tak":
            return blessing


def utworz_postac():
    wypisz("DUNGEONS OF AVAMAST", kolor="YELLOW", styl="BOLD", opoznienie=0.01)
    wypisz(
        "Witaj w Dungeons of Avamast! Zanim rozpoczniesz swoją przygodę, musisz stworzyć swojego bohatera.",
        styl="NONE",
        opoznienie=0.02,
    )

    player_name = wybierz_imie_gracza()
    strength, dexterity, intelligence = wybierz_statystyki()
    blessing = wybierz_blogoslawienstwo()
    return Player(player_name, strength, dexterity, intelligence, blessing)
