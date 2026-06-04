# ⚔️ DungeonsOfAvamast — silnik tekstowego RPG (MVP)

Projekt to autorski silnik RPG w Pythonie. W tej chwili projekt jest w stanie MVP i zawiera grywalny samouczek oraz podstawowe mechaniki rozgrywki.

**Główne cechy (aktualny stan)**
- Grywalny samouczek: interaktywne wprowadzenie do mechanik i sterowania (`tutorial.py`).
- Podstawowa pętla gry i system menu (`start.py`, `main.py`).
- System tworzenia postaci i wyświetlania statystyk (`kreator.py`, `characters.py`).
- Prosty system walki i testowe potwory (`fights.py`, `monsters.py`).
- Moduły przedmiotów i broni (`items.py`, `weapons.py`).
- Mapy i lokacje w rozwoju (`mapa.py`, `lokacjewiz.py`).

**Techniczne wymagania**
- Python 3.12 (zalecane).
- Virtual environment (opcjonalnie, ale rekomendowane).

**Szybki start (Windows PowerShell)**
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python start.py
```

Alternatywnie uruchom `python main.py` z aktywowanym środowiskiem, ale domyślnym punktem startowym jest `start.py`.

**Pliki warte uwagi**
- `start.py` — główne uruchomienie gry i wybór pominięcia samouczka.
- `main.py` — główna pętla gry i logika po samouczku.
- `tutorial.py` — moduł samouczka.
- `kreator.py` / `characters.py` — tworzenie postaci i statystyki.
- `fights.py` / `monsters.py` — system walki i przykładowe potwory.
- `items.py` / `weapons.py` — ekwipunek i bronie.

**Jak rozwijać projekt**
- Dodać trwały system zapisu/ładowania stanu gry (serialization).
- Rozbudować system statystyk i obliczania obrażeń.
- Przenieść zawartość gry do plików danych (JSON/YAML) dla łatwej edycji.
- Dalsze prace nad mapami, zagadkami i contentem.

Jeśli chcesz, mogę: uruchomić prosty test, dodać `requirements.txt`, albo przygotować szablon JSON do definiowania potworów i przedmiotów.

---
_Plik zaktualizowany automatycznie aby odzwierciedlać bieżący stan projektu._
