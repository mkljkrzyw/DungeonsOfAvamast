from monsters import rapax
from ui import wypisz
from bestiariusz import *
import os
def azurith():
    wypisz('''
    OPIS
    Azurith to nadmorski region z wieloma wyspami.  Na większości wysp znajdują się wioski lub na większych wyspach miasta. Mieszkańcy Azurith są wspaniałymi żeglażami i potrafią przemieszczać się bardzo szybko pomiędzy wioskami. Ucząc się na błędach postawili na wielu wyspach strażnice, z których wypatruje się, czy nie zbliża się zagrożenie. W razie ataku od razu rozpalane jest ognisko dzięki któremu alarm przekazywany jest aż do stolicy że państwo zostało zaatakowane. Mają wiele regionalnych potraw. Najbardziej znaną są ślimaki morskie \n
    "GOSPODARKA"
    Głównym zarobkiem mieszkańców są ryby, które głównie służą jako pożywienie, jednak istnieją również rzadkie gatunki ryb o magicznych właściwościach, które wykupują magowie, ponieważ tworzone są mikstury.
    STOLICA
    Stolica Azurith leży na półwyspie, co powoduje że lądem można ją zaatakować wyłącznie z frontu gdzie znajduje się całe ufortowanie. Od ataku Valandoru  cała okolica jest patrolowana i chroniona przez specjalne statki stworzone wyłącznie do walki. 
            ''', slowo_bold=["OPIS", "GOSPODARKA", "STOLICA"], slowo_kolor={"OPIS": "CYAN", "GOSPODARKA": "CYAN", "STOLICA": "CYAN"})
def bestie():
    best=""
    while True:
        while best not in ["1", "2"]:
            os.system("cls")
            wypisz("Bestiariusz", styl="BOLD", kolor="YELLOW")
            wypisz("O czym chcesz przeczytać?")
            wypisz("1. Rapax")
            wypisz("2. Powrót")
            best=input("> ")
            if best == "1":
                os.system("cls")
                wypisz("WYGLĄD: \n"+rapax().visual+"\n")
                wypisz("ZACHOWANIE: \n"+rapax().behavior+"\n")
                wypisz("KLASYFIKACJA: \n"+rapax().clasification+"\n")
                wypisz("SZKIC: \n"+rapax().image+"\n")
                wypisz("Naciśnij Enter, aby wrócić do poprzedniego menu.")
                input()
                os.system("cls")
                best=""
            elif best == "2":
                os.system("cls")
                return
def kampania():
    wypisz("VALANDORSKA KAMPANIA WOJENNA I JEJ KONSEKWENCJE", styl="BOLD", kolor="YELLOW")
    wypisz('''
Od swojego powstania Valandor nieustannie narastał w siłę. W ów czasach nie było armii równej tej, należącej do Państwa Centralnego. Drugi Valandorski władca uznał, to właśnie jego region powinien czerpać garściami z całego kontynentu. Choć wielu strategów, mędrców i weteranów spodziewało się wojen trwających latami, przeciągających się z pokolenia na pokolenie, cała kampania skończyła się po zaledwie kilku latach. 

Azurith nigdy nie był państwem skłonnym do wojen. Poddał się bez walki i zgodził się na warunki postawione przez Valandor. Od tamtej pory płaci Państwu Centralnemu regularne podatki. Wbrew wszelkim oczekiwaniom Azurith szybko zaczął czerpać ogromne zyski z nowego porządku. Ludność z całego kontynentu zjeżdżała się do nadmorskiego regionu w poszukiwaniu korzystnych cen, które oczywiście odnajdywała. Kieszenie handlarzy zapełniały się szybciej niż skarbiec Państwa Centralnego.

Auroria, jako najmłodszy i najmniej zaludniony region, nie posiadała armii. Jej mieszkańcy byli przeciwni rozlewowi krwi i podporządkowała się Valandorowi stając się państwem satelitarnym.

Magorath było prężnie rozwijającym się regionem i to właśnie dlatego ucierpiało najbardziej. Stawił opór i zapłacił za to tysiącami istnień. Żyzne ziemie spłynęły krwią choć wojna od samego początku była przesądzona. Po klęsce Magorath stało się niczym więcej niż olbrzymią Valandorską farmą.

Arkanya podjęła walkę choć szybko z niej zrezygnowała. Po pierwszej bitwie na własnej skórze przekonała się jak potężna jest Valandorska armia. W celu zapobiegnięciu dalszemu rozlewowi krwi, uznała wyższość Pańswa Centralnego. Podobnie jak Azurith płaci podatek.

Thailandor, ze względu na swój surowy klimat, wysokie góry i godną podziwu waleczność mieszkańców jako jedyny zdołał odeprzeć inwazję. Do dziś dzień jest jedynym regionem z którym Valandor nie był w stanie się uporać, nawet w czasach swojej świetności.

Sylvanar natomiast nigdy nie został zaatakowany. Górzyste pustkowia regionu sprawiły, że uznano go za teren niebezpieczny i niewarty działań wojennych. Pomimo tego, Sylvanar do dziś ponosi ogromne straty gospodarcze, zmuszony płacić wysokie cła na kontrolowanych przez Valandor szlakach handlowych.
''', slowo_bold=["Azurith", "Auroria", "Magorath", "Arkanya", "Thailandor", "Sylvanar"], slowo_kolor={"Azurith": "CYAN", "Auroria": "CYAN", "Magorath": "CYAN", "Arkanya": "CYAN", "Thailandor": "CYAN", "Sylvanar": "CYAN"})
    wypisz("\nNaciśnij Enter, aby wrócić do poprzedniego menu.")
    input()
    os.system("cls")