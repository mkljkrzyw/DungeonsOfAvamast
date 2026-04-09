# ⚔️ DungeonsOfAvamast - Text-Based RPG Engine (Core Foundation) 

To jest projekt autorskiego silnika RPG napisanego w Pythonie. Obecnie projekt znajduje się w fazie **MVP (Minimum Viable Product)** i zawiera grywalny moduł samouczka, który prezentuje główne mechaniki gry.

## 🏗️ Obecny Stan Projektu (Core Features)
- **Engine Logic:** Podstawowa pętla gry (Game Loop) zarządzająca stanem gracza.
- **Tutorial Module:** Interaktywne wprowadzenie do mechanik świata i sterowania.
- **Input System:** Obsługa i walidacja komend użytkownika.
- **Modular Architecture:** Kod podzielony na klasy (OOP), co pozwala na łatwe dodawanie nowych lokacji, przedmiotów i przeciwników bez przebudowy całego systemu.

## 🛠️ Stack Techniczny
- **Język:** Python 3.12
- **Paradygmat:** Programowanie Obiektowe (OOP) – nacisk na czysty i czytelny kod.

## 🚀 Roadmap: Co dalej? (Wizja Rozwoju)
1. **System Statystyk i Walki:** Wprowadzenie algorytmów obliczających obrażenia na podstawie atrybutów.
2. **Data-Driven Content:** Przeniesienie opisów świata i statystyk do zewnętrznych plików JSON/YAML (łatwiejsza edycja).
3. **AI Integration (Cel Główny):** Wykorzystanie modeli LLM (np. przez API OpenAI) do generowania unikalnych dialogów i opisów otoczenia, aby każda rozgrywka była inna.
4. **Proceduralne Wydarzenia:** Skrypty generujące losowe spotkania na mapie świata.
