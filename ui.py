import re
import sys
import os
import time
import colorama

from DungeonsOfAvamast.monsters import rapax

try:
    import msvcrt
except ImportError:
    msvcrt = None


colorama.just_fix_windows_console()

COLORS = {
    "RED": "\033[91m",
    "GREEN": "\033[92m",
    "YELLOW": "\033[93m",
    "BLUE": "\033[94m",
    "PURPLE": "\033[95m",
    "CYAN": "\033[96m",
    "LIGHT_GREEN": "\033[92m",
    "RESET": "\033[0m",
}

STYL = {
    "BOLD": "\033[1m",
    "UNDERLINE": "\033[4m",
    "NONE": "",
}

YELLOW = COLORS["YELLOW"]
GREEN = COLORS["GREEN"]
LIGHT_GREEN = COLORS["LIGHT_GREEN"]
CYAN = COLORS["CYAN"]
RESET = COLORS["RESET"]


def _normalizuj_kod_koloru(kolor, domyslny):
    if kolor is None:
        return domyslny
    kolor_txt = str(kolor).strip()
    if not kolor_txt:
        return domyslny
    return COLORS.get(kolor_txt.upper(), COLORS["RESET"])


def _normalizuj_slowa(wartosci):
    if not wartosci:
        return []
    if isinstance(wartosci, dict):
        wartosci = list(wartosci.keys())
    if isinstance(wartosci, str):
        return [wartosc.strip() for wartosc in wartosci.split(";") if wartosc.strip()]

    wynik = []
    for wartosc in wartosci:
        wartosc_txt = str(wartosc).strip()
        if wartosc_txt:
            wynik.append(wartosc_txt)
    return wynik


def _normalizuj_kolory(wartosci, domyslny_kolor):
    if not wartosci:
        return {}

    if isinstance(wartosci, dict):
        wynik = {}
        for fraza, kolor in wartosci.items():
            fraza_txt = str(fraza).strip()
            if not fraza_txt:
                continue
            wynik[fraza_txt] = _normalizuj_kod_koloru(kolor, domyslny_kolor)
        return wynik

    if isinstance(wartosci, (list, tuple, set)):
        lista_wartosci = list(wartosci)
        if lista_wartosci and all(isinstance(element, tuple) and len(element) == 2 for element in lista_wartosci):
            wynik = {}
            for fraza, kolor in lista_wartosci:
                fraza_txt = str(fraza).strip()
                if not fraza_txt:
                    continue
                wynik[fraza_txt] = _normalizuj_kod_koloru(kolor, domyslny_kolor)
            return wynik

        return {
            str(fraza).strip(): domyslny_kolor
            for fraza in lista_wartosci
            if str(fraza).strip()
        }

    fraza_txt = str(wartosci).strip()
    if not fraza_txt:
        return {}
    return {fraza_txt: domyslny_kolor}


def _granica_slowa(tekst, start, end):
    przed = tekst[start - 1] if start > 0 else ""
    po = tekst[end] if end < len(tekst) else ""
    return not (przed.isalnum() or przed == "_") and not (po.isalnum() or po == "_")


def _znajdz_zakresy(tekst, fraza):
    zakresy = []
    if not fraza:
        return zakresy

    wzorzec = re.compile(re.escape(fraza), flags=re.IGNORECASE)
    czy_pojedyncze_slowo = bool(re.fullmatch(r"\w+", fraza, flags=re.UNICODE))

    for dopasowanie in wzorzec.finditer(tekst):
        start, end = dopasowanie.span()
        if czy_pojedyncze_slowo and not _granica_slowa(tekst, start, end):
            continue
        zakresy.append((start, end))

    return zakresy


def _czy_enter_nacisnienty():
    if msvcrt is None:
        return False
    try:
        if msvcrt.kbhit():
            klawisz = msvcrt.getch()
            if klawisz == b'\r' or klawisz == b'\n':
                return True
    except Exception:
        pass
    return False


def wypisz(
    tekst,
    kolor="RESET",
    styl="NONE",
    opoznienie=0.02,
    slowo_bold=None,
    slowo_kolor=None,
    kolor_slowa=None,
):
    tekst = str(tekst)
    kod_koloru = _normalizuj_kod_koloru(kolor, COLORS["RESET"])
    kod_stylu = STYL.get(str(styl).upper(), STYL["NONE"])
    kod_reset = COLORS["RESET"]
    bazowy_prefiks = kod_stylu + kod_koloru

    frazy_bold = _normalizuj_slowa(slowo_bold)
    mapowanie_kolorow = _normalizuj_kolory(slowo_kolor, _normalizuj_kod_koloru(kolor_slowa, kod_koloru))

    bold_maska = [False] * len(tekst)
    kolor_maska = [None] * len(tekst)

    for fraza in sorted(frazy_bold, key=len, reverse=True):
        for start, end in _znajdz_zakresy(tekst, fraza):
            for idx in range(start, end):
                bold_maska[idx] = True

    for fraza, kod_koloru_frazy in sorted(mapowanie_kolorow.items(), key=lambda el: len(el[0]), reverse=True):
        for start, end in _znajdz_zakresy(tekst, fraza):
            for idx in range(start, end):
                if kolor_maska[idx] is None:
                    kolor_maska[idx] = kod_koloru_frazy

    sys.stdout.write(bazowy_prefiks)

    aktywny_prefiks = bazowy_prefiks
    ostatni_check_klawisza = time.time()
    pominac_opoznienie = False

    for idx, znak in enumerate(tekst):
        prefiks_znaku = ""
        if bold_maska[idx]:
            prefiks_znaku += STYL["BOLD"]
        prefiks_znaku += kolor_maska[idx] if kolor_maska[idx] else kod_koloru

        if prefiks_znaku != aktywny_prefiks:
            sys.stdout.write(kod_reset + prefiks_znaku)
            aktywny_prefiks = prefiks_znaku

        sys.stdout.write(znak)
        sys.stdout.flush()

        # Sprawdzaj klawisz co 0.05s
        teraz = time.time()
        if teraz - ostatni_check_klawisza >= 0.05:
            if _czy_enter_nacisnienty():
                pominac_opoznienie = True
            ostatni_check_klawisza = teraz

        # Jeśli Enter wciśnięty, wypisz resztę bez opóźnień
        if not pominac_opoznienie:
            time.sleep(opoznienie)

    sys.stdout.write(kod_reset + "\n")
    sys.stdout.flush()
def bestiariusz():
    os.system("cls")
    wypisz("O czym chcesz przeczytać? \n1. Rapax \n 2. Powrót", slowo_kolor={"Rapax": "YELLOW"})
    best=input("> ")
    while best not in ["1", "2"]:
        os.system("cls")
        wypisz("O czym chcesz przeczytać? \n1. Rapax \n 2. Powrót", slowo_kolor={"Rapax": "YELLOW"})
        best=input("> ")
        if best == "1":
            wypisz(rapax().visual, slowo_kolor={rapax().visual: "YELLOW"})
            wypisz(rapax().behavior, slowo_kolor={rapax().behavior: "YELLOW"})
            wypisz(rapax().clasification, slowo_kolor={rapax().clasification: "YELLOW"})
        elif best == "2":
            return
def help():
    wypisz('''
Dungeons of Avamast
=================
Commands:
    go [direction]  - poruszanie się w danym kierunku (np. "go north")
    get [item]      - podniesienie przedmiotu (np. "get key")
    use [item]      - użycie przedmiotu z pokoju, lub ekwipunku (np. "use key")
    inventory       - wyświetlenie zawartości ekwipunku
    stats           - wyświetlenie statystyk postaci
    info            - wyświetlenie informacji o aktualnej lokalizacji
    help            - wyświetlenie tej pomocy
''', slowo_bold="go;get;use;inventory;stats;info;help", slowo_kolor={"Dungeons of Avamast": "YELLOW", "go": "GREEN", "get": "GREEN", "use": "GREEN", "inventory": "YELLOW", "stats": "YELLOW", "info": "CYAN", "help": "CYAN"}, kolor="RESET", styl="BOLD")