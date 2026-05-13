import os
import random
from blogoslawienstwa import krew, oczy, ciezar
from ui import wypisz, bestiariusz

turagracz=""
turapotwora=""
czy_crit=False
def walka(player, przeciwnik):
    turagracz = ""
    turapotwora = ""
    czy_crit = False
    wypisz(f"Rozpoczynasz walkę z {przeciwnik.name}!")
    if player.dexterity > przeciwnik.dexterity:
        atakujacy = player
    else:
        atakujacy = przeciwnik
        action=random.randint(1, 3)
    while player.hp > 0 and przeciwnik.hp > 0:
        if atakujacy == player:
            print(f"\n{player.name} HP: {player.hp}/{player.max_hp} | {przeciwnik.name} HP: {przeciwnik.hp}/{przeciwnik.max_hp}")
            print("1. Atakuj")
            print("2. Użyj blogosławieństwa")
            print("3. Użyj przedmiotu")
            print("4. Broń się")
            print("5. Unikaj")
            print("6. Ucieczka")
            choice = input("> ").strip()
            if choice == "1":
                    if random.randint(1, 100) >= 90:
                        print(f"Wykonujesz potężny atak!")
                        player_damage = player.damage * 2
                        czy_crit=True
                    else:
                        player_damage=random.randint(player.damage-3, player.damage+3)
                    if turapotwora=="obrona":
                        print(f"Atakujesz, ale {przeciwnik.name} broni się przed atakiem!")
                        player_damage=player_damage//2
                        turapotwora=""
                        if czy_crit==True:
                            wypisz(f"Wykonujesz potężny atak, ale {przeciwnik.name} broni się przed atakiem! Otrzymuje tylko {player_damage} obrażeń!",opoznienie=0, slowo_kolor={f"{player_damage} obrażeń": "GREEN"})
                            czy_crit=False
                        else:
                            wypisz(f"Zadajesz tylko {player_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{player_damage} obrażeń": "GREEN"})
                            czy_crit=False
                            
                    else:
                        if czy_crit==True:
                            wypisz(f"Wykonujesz potężny atak. {przeciwnik.name} otrzymuje {player_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{player_damage} obrażeń": "GREEN"})
                            czy_crit=False
                        else:
                            wypisz(f"Zadajesz {player_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{player_damage} obrażeń": "GREEN"})
                            czy_crit=False
                    przeciwnik.hp -= player_damage
            elif choice == "2":
                if player.energy >= 10:
                    if player.blessing == "krew":
                        krew()
                    elif player.blessing == "oczy":
                        oczy()
                        if przeciwnik.name=="Rapax":
                            wypisz("Nagle dociera do Ciebie, że ta walka to Twój koniec, ale też wyzwolenie z tego dziwnego miejsca. ")
                    elif player.blessing == "ciezar":
                        ciezar()
            elif choice == "3":
                print("Ekwipunek:")
                for each, item in enumerate(player.inventory, 1):
                    print(f"{each}. {item}")
                item_choice = input("Wybierz przedmiot do użycia (numer): ").strip()
                for each, item in enumerate(player.inventory, 1):
                    if item_choice == str(each):
                        if item == "piwo":
                            print("Pijesz piwo i czujesz się odświeżony.")
                            if player.hp + 5 > player.max_hp:
                                player.hp = player.max_hp
                            player.hp +=5
                            player.inventory.remove(item)
                        elif item == "bestiariusz":
                            bestiariusz()
                        else:
                            print(f"Używasz {item} z ekwipunku, ale nic się nie dzieje.")
                    else:
                        print("Nie masz takiego przedmiotu w ekwipunku.")
            elif choice == "4":
                print("Udaje ci się obronić przed atakiem!")
                turagracz="obrona"
            elif choice == "5":
                if random.randint(1, 100) <= player.dexterity * 2:
                    print("Unikasz ataku!")
                else:
                    print("Nie udało się uniknąć ataku!")
            elif choice == "6":
                if przeciwnik.name == "Rapax":
                    wypisz("Nie możesz uciec przed Rapaxem!")
                else:
                    if random.randint(1, 100) <= player.dexterity:
                        print("Udało Ci się uciec!")
                    break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        
            atakujacy = przeciwnik
        if atakujacy == przeciwnik:
            if przeciwnik.strength==0:
                print(f"{przeciwnik.name} stoi bezczynnie, nie zadaje obrażeń.")
                przeciwnik.hp =przeciwnik.max_hp
            else:
                action=random.randint(1, 3)
                if action == 1:
                    if random.randint(1, 100) >= 90:
                        print(f"{przeciwnik.name} wykonuje potężny atak!")
                        enemy_damage = przeciwnik.damage * 2
                        czy_crit=True
                    else:
                        enemy_damage=random.randint(przeciwnik.damage-3, przeciwnik.damage+3)
                    if turagracz=="obrona":
                        print(f"{przeciwnik.name} atakuje, ale Ty bronisz się przed atakiem!")
                        enemy_damage=enemy_damage//2
                        turagracz=""
                        if czy_crit==True:
                            wypisz(f"{przeciwnik.name} wykonuje potężny atak, ale Ty bronisz się przed atakiem! Otrzymujesz tylko {enemy_damage} obrażeń!",opoznienie=0, slowo_kolor={f"{enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                        else:
                            wypisz(f"{przeciwnik.name} zadaje Ci tylko {enemy_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                            
                    else:
                        if czy_crit==True:
                            wypisz(f"{przeciwnik.name} wykonuje potężny atak. Otrzymujesz {enemy_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                        else:
                            wypisz(f"{przeciwnik.name} zadaje Ci {enemy_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                    player.hp -= enemy_damage
                elif action == 2:
                    turapotwora="obrona"
                    print(f"{przeciwnik.name} broni się przed Twoim atakiem!")
                elif action == 3:
                    if random.randint(1, 100) <= przeciwnik.dexterity * 2:
                        print(f"{przeciwnik.name} unika ataku!")
                    else:
                        print(f"{przeciwnik.name} nie dał rady uniknąć ataku!")
            atakujacy = player
    if player.hp <= 0:
        print("Zostałeś pokonany! Game Over.")
        
    else:        
        print("Wygrałeś walkę!")