import os
import random
from przedmioty import blogoslawienstwa
from przedmioty.blogoslawienstwa import krew, oczy, ciezar
from interfejs.ui import wypisz, bestiariusz, opisz_przedmiot
from przedmioty.items import *
os.system("cls")
turagracz=""
turapotwora=""
czy_crit=False
licznik=0
def walka(player, przeciwnik):
    if isinstance(przeciwnik, type):
        przeciwnik = przeciwnik()

    turagracz = ""
    turapotwora = ""
    czy_crit = False
    player.currentdefense = player.defense
    przeciwnik.currentdefense = przeciwnik.defense
    wypisz(f"Rozpoczynasz walkę z {przeciwnik.name}!")
    if player.dexterity > przeciwnik.dexterity:
        atakujacy = player
    else:
        atakujacy = przeciwnik
        action=random.randint(1, 3)
    while player.hp > 0 and przeciwnik.hp > 0:
        if atakujacy == player:
            print(f"\n{player.name} HP: {player.hp}/{player.max_hp} Energia: {player.energy}/{player.max_energy} | {przeciwnik.name} HP: {przeciwnik.hp}/{przeciwnik.max_hp}")
            print("1. Atakuj")
            print("2. Użyj blogosławieństwa")
            print("3. Użyj przedmiotu")
            print("4. Broń się")
            print("5. Unikaj")
            print("6. Ucieczka")
            choice = input("> ").strip()
            os.system("cls")
            if choice == "1":
                    if(player.blessing=="Manipulacja krwią" and blogoslawienstwa.uderzenie==True):
                            player_damage = player.wzmocniony_dmg
                            blogoslawienstwa.uderzenie=False
                    elif(player.blessing=="Manipulacja krwią" and blogoslawienstwa.zwiekszenie==True):
                            player_damage = player.currentdmg
                            licznik+=1
                            if licznik%3==0:
                                player.currentdmg=player.currentdmg/1.2
                                blogoslawienstwa.zwiekszenie=False
                            blogoslawienstwa.zwiekszenie=False
                    elif(player.blessing=="Oczy przyszłości" and blogoslawienstwa.unikanie==True):
                            blogoslawienstwa.unikanie=False
                            player_damage = player.damage
                    elif(player.blessing=="Oczy przyszłości" and blogoslawienstwa.zwiekszenie==True):
                            player_damage = player.currentdmg
                            licznik+=1
                            if licznik%3==0:
                                player.currentdmg=player.currentdmg/1.2
                                blogoslawienstwa.zwiekszenie=False
                            blogoslawienstwa.zwiekszenie=False
                    elif(player.blessing=="Manipulacja ciężarem" and blogoslawienstwa.uderzenie==True):
                            player_damage = player.currentdmg * 5
                            blogoslawienstwa.uderzenie=False
                    if random.randint(1, 100) >= 90:
                        print(f"Wykonujesz potężny atak!")
                        
                        player_damage = player.damage * 2
                        czy_crit=True
                    else:
                        los=random.randint(player.damage-3, player.damage+3)
                        if los < 0:
                            player_damage = 0
                        else:
                            player_damage = los
                    if turapotwora=="obrona":
                        print(f"Atakujesz, ale {przeciwnik.name} broni się przed atakiem!")
                        player_damage=player_damage//2
                        turapotwora=""
                        final_damage = int(player_damage / (1 + przeciwnik.currentdefense * 0.1))
                        if czy_crit==True:
                            wypisz(f"Wykonujesz potężny atak, ale {przeciwnik.name} broni się przed atakiem! Otrzymuje tylko {final_damage} obrażeń! (KRYTYCZNY)",opoznienie=0, slowo_kolor={f"{final_damage} obrażeń": "YELLOW"})
                            czy_crit=False
                        else:
                            wypisz(f"Zadajesz tylko {final_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{final_damage} obrażeń": "GREEN"})
                            czy_crit=False
                            
                    else:
                        final_damage = int(player_damage / (1 + przeciwnik.currentdefense * 0.1))
                        if czy_crit==True:
                            wypisz(f"Wykonujesz potężny atak. {przeciwnik.name} otrzymuje {final_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{final_damage} obrażeń! (KRYTYCZNY)": "YELLOW"})
                            czy_crit=False
                        else:
                            wypisz(f"Zadajesz {final_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{final_damage} obrażeń": "GREEN"})
                            czy_crit=False
                    przeciwnik.hp -= final_damage
                    player_damage=player.damage
                    przeciwnik.currentdefense=przeciwnik.defense
            elif choice == "2":
                if player.energy >= 10:
                    print("Używasz swojego błogosławieństwa!")
                    if player.blessing == "Manipulacja krwią":
                        #print("krew")
                        krew(player)
                    elif player.blessing == "Oczy przyszłości":
                        #print("oczy")
                        oczy(player)
                        if przeciwnik.name=="Rapax":
                            wypisz("Nagle dociera do Ciebie, że ta walka to Twój koniec, ale też wyzwolenie z tego dziwnego miejsca. ")
                    elif player.blessing == "Manipulacja ciężarem":
                        #print("ciezar")
                        ciezar(player)
                else:
                    wypisz("Nie masz wystarczająco energii, aby użyć błogosławieństwa!", slowo_kolor={"Nie masz wystarczająco energii, aby użyć błogosławieństwa!": "RED"})
            elif choice == "3":
                print("Ekwipunek:")
                for each, item in enumerate(player.inventory, 1):
                    print(f"{each}. {opisz_przedmiot(item)}")
                item_choice = input("Wybierz przedmiot do użycia (numer): ").strip()
                for each, item in enumerate(player.inventory, 1):
                    if item_choice == str(each):
                        if item == "piwo":
                            piwo(player)
                            player.inventory.remove(item)
                        elif item == "bestiariusz":
                            bestiariusz()
                        else:
                            wypisz(f"Używasz {item} z ekwipunku, ale nic się nie dzieje.", slowo_kolor={f"{item}": "YELLOW"})
                    else:
                        wypisz("Nie masz takiego przedmiotu w ekwipunku.", slowo_kolor={"Nie masz takiego przedmiotu w ekwipunku.": "RED"})
            elif choice == "4":
                print("Udaje ci się obronić przed atakiem!")
                turagracz="obrona"
            elif choice == "5":
                if random.randint(1, 100) <= player.dexterity * 2:
                    player.currentdefense = 9999999
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
                        final_enemy_damage = int(enemy_damage / (1 + player.currentdefense * 0.1))
                        if czy_crit==True:
                            wypisz(f"{przeciwnik.name} wykonuje potężny atak, ale Ty bronisz się przed atakiem! Otrzymujesz tylko {final_enemy_damage} obrażeń! (KRYTYCZNY)",opoznienie=0, slowo_kolor={f"{final_enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                        else:
                            wypisz(f"{przeciwnik.name} zadaje Ci tylko {final_enemy_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{final_enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                            
                    else:
                        final_enemy_damage = int(enemy_damage / (1 + player.currentdefense * 0.1))
                        if czy_crit==True:
                            wypisz(f"{przeciwnik.name} wykonuje potężny atak. Otrzymujesz {final_enemy_damage} obrażeń! (KRYTYCZNY)", opoznienie=0,slowo_kolor={f"{final_enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                        else:
                            wypisz(f"{przeciwnik.name} zadaje Ci {final_enemy_damage} obrażeń!", opoznienie=0,slowo_kolor={f"{final_enemy_damage} obrażeń": "RED"})
                            czy_crit=False
                    player.hp -= final_enemy_damage
                    player.currentdefense=player.defense
                elif action == 2:
                    turapotwora="obrona"
                    print(f"{przeciwnik.name} broni się przed Twoim atakiem!")
                elif action == 3:
                    if random.randint(1, 100) <= przeciwnik.dexterity * 2:
                        print(f"{przeciwnik.name} unika ataku!")
                        przeciwnik.currentdefense = 9999999
                    else:
                        print(f"{przeciwnik.name} nie dał rady uniknąć ataku!")
            atakujacy = player
    if player.hp <= 0:
        print("Zostałeś pokonany!")
        if przeciwnik.name=="Rapax":
            return
        else:
            exit()
        
    else:        
        print("Wygrałeś walkę!")
        player.exp += przeciwnik.exp
        player.gold += getattr(przeciwnik, "gold", 0)
        wypisz(f"Otrzymujesz {przeciwnik.exp} doświadczenia!", slowo_kolor={f"{przeciwnik.exp} doświadczenia!": "GREEN"})
        if getattr(przeciwnik, "gold", 0):
            wypisz(f"Otrzymujesz {przeciwnik.gold} złota!", slowo_kolor={f"{przeciwnik.gold} złota!": "YELLOW"})
        player.currentdefense = player.defense
        wypisz("Naciśnij Enter, aby kontynuować...")
        input()
        