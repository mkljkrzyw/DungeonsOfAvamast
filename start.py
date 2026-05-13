from characters import Player
from kreator import zapytaj_tak_nie, utworz_postac, wyczysc_ekran
from tutorial import tutorial
from ui import wypisz
from main import main


def uruchom_gre():
    wyczysc_ekran()
    player = utworz_postac()
    player.show_stats()
    wypisz("=" * 30)
    while True:
        wypisz("Czy chcesz pominąć samouczek? (tak/nie)", slowo_bold="tak/nie", slowo_kolor={"tak": "GREEN", "nie": "RED"})
        odpowiedz = input("> ").strip().lower()
        if odpowiedz in ["tak", "nie"]:
            return odpowiedz
        else:
             wyczysc_ekran()
             wypisz("Proszę wpisać 'tak' lub 'nie'.")
        if odpowiedz == "tak":
            wypisz("Pominięto samouczek. Powodzenia w Dungeons of Avamast!")
            main()
        elif odpowiedz == "nie":
            wyczysc_ekran()
            tutorial(player)


def main():
    print("Tryb testowy: (tak/nie)")
    if input("> ").strip().lower() == "tak":
        player = Player("Testowy Bohater", 10, 10, 10, "Brak")
        tutorial(player)
        return
    wyczysc_ekran()
    uruchom_gre()
    


if __name__ == "__main__":
    main()