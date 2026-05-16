from characters import Player
from kreator import zapytaj_tak_nie, utworz_postac, wyczysc_ekran
from tutorial import tutorial
from ui import wypisz
from main import main
from fights import walka
from monsters import test

def uruchom_gre():
    wyczysc_ekran()
    wypisz("Nikt nie pamięta, kiedy pojawiła się na Avamast.", opoznienie=0.05, slowo_bold="Avamast", slowo_kolor={"Avamast": "YELLOW"})
    wypisz("Nie istnieją kroniki opisujące jej początek, ani żadne słowa tych którzy widzieli ją po raz pierwszy.", opoznienie=0.05)

    wypisz("Jedni twierdzą że jest karą zesłaną za ludzkie grzechy, inni dopatrują się w niej części Boskiego planu, możliwością dostąpienia zbawienia. Burza, jak zwykliśmy ją nazywać, przeszło 700 lat temu gwałtownie nabrała na sile. Nim magowie zdążyli podjąć działanie, pochłonęła lwią część wschodnich ziem zmuszając ludzi do ucieczki na zachód. Z każdym rokiem stawała się coraz bardziej zachłanna, sięgała swoimi mackami coraz dalej i dalej, zatruwała naszą ziemię jak zaraza, na którą nigdy nie odnaleziono lekarstwa. Wysyłała swoich bękartów, a ci nie znali litości. Mordowali naszych przodków bez mrugnięcia okiem, żywili się ich ciałami i napawali się ich agonalnym krzykiem. Całe miasta znikały w ciągu jednej nocy.", opoznienie=0.05, slowo_bold="Burza", slowo_kolor={"Burza": "RED"})
    print("")
    wypisz("To właśnie wtedy powstał Zakon.",opoznienie=0.05, slowo_bold="Zakon", slowo_kolor={"Zakon": "YELLOW"})

    wypisz("Magowie odkryli bowiem, że niektóre dzieci rodzą się inne. Naznaczone czymś, czego do dziś najwięksi mędrcy nie potrafią wytłumaczyć. W ich duszach tkwi moc przypominająca magię, choć w rzeczywistości nie ma z nią nic wspólnego. Zaczęto wzniośle nazywać je błogosławionymi. Nie czeka ich jednak życie bohaterów ani dumna walka w imię dobra. Ich przeznaczenie jest bliższe wyrokowi niż zaszczytowi - dożywotnia tułaczka. Jeszcze jako dzieci zabierane są do Ezelthorn, głównej siedziby Zakonu. Tam przechodzą brutalne szkolenia których część nie przeżywa. Słabi umierają, silni natomiast stają się wojownikami. A gdy nadejdzie odpowiedni moment, odbiera im się część człowieczeństwa. Wypalana jest im jedna gałka oczna. W jej miejsce wszczepia się Oko Cherubina. To właśnie temu zakonnicy zawdzięczają sobie przydomek Cherubinów. Jest ona niewielką obsydianową kulą zdolną magazynować mroczną energię. Dzięki niej błogosławieństwo może zostać okiełznane. Dzięki niej dzieci stają się bronią.", opoznienie=0.05, slowo_bold="Cherubinów; Ezelthorn", slowo_kolor={"Cherubinów": "YELLOW", "Ezelthorn": "YELLOW"})
    print("")
    wypisz("Minęło 700 lat od chwili, w której powstał Zakon. Przez ten czas przelano całe oceany krwi. Upadały królestwa, płonęły miasta, całe pokolenia Cherubinów ginęły. A mimo to zagrożenie nigdy nie zniknęło. Burza choć w ryzach, nadal stara się rosnąć. Otacza ziemie ludzkości niczym pętla na szyi wisielca... zaciska się... powoli. ", opoznienie=0.05)
    print("")
    wypisz("Zwykli ludzie nie wiedzą.",opoznienie=0.08, styl="BOLD", kolor="RED")

    wypisz("Każdy kto pamiętał o zakonie od setek lat gnije pod ziemią. Magowie zadbali o to, by prawda została zatajona. Istnienie potworów, podobnie jak zakonu jest utrzymywana w tajemnicy. Mówią, że chronią ich od paniki i strachu, że zapewniają im spokój. ", opoznienie=0.05)
    print("")
    wypisz("Ludzkość więc hodowana jest w iluzji spokoju. Jak świnie hodowane na łąkach nieświadome czekającego ich losu.", opoznienie=0.05)
    print("")
    wypisz("A my wciąż walczymy.", opoznienie=0.09, styl="BOLD", kolor="YELLOW")
    print("\n\n Aby kontynuować, naciśnij Enter...")
    input()
    wyczysc_ekran()
    player = utworz_postac()
    player.show_stats()
    wypisz("=" * 30)
    while True:
        wypisz("Czy chcesz pominąć samouczek? (tak/nie)", slowo_bold="tak/nie", slowo_kolor={"tak": "GREEN", "nie": "RED"})
        odpowiedz = input("> ").strip().lower()
        if odpowiedz in ["tak", "nie"]:
            if odpowiedz == "tak":
                wypisz("Pominięto samouczek. Powodzenia w Dungeons of Avamast!")
                main(player)
            elif odpowiedz == "nie":
                wyczysc_ekran()
                tutorial(player)
        else:
             wyczysc_ekran()
             wypisz("Proszę wpisać 'tak' lub 'nie'.")
        


def start():
    print("Tryb testowy: (tak/nie)")
    if input("> ").strip().lower() == "tak":
        print("Samouczek? (tak/nie)")
        if input("> ").strip().lower() == "tak":
            player = Player("Testowy Bohater", 10, 10, 10, "Manipulacja krwią")
            tutorial(player)
            return
        else:
            print("Walka? (tak/nie)")
            if input("> ").strip().lower() == "tak":
                player = Player("Testowy Bohater", 10, 10, 10, "Manipulacja krwią")
                walka(player, test)
            else:
                player = Player("Testowy Bohater", 10, 10, 10, "Manipulacja krwią")
                main(player)
    wyczysc_ekran()
    uruchom_gre()
    


if __name__ == "__main__":
    start()