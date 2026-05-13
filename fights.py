import os
import random


def walka(player, przeciwnik):
    print(f"Rozpoczynasz walkę z {przeciwnik.name}!")
    if player.dexterity > przeciwnik.dexterity:
        atakujacy = player
    else:
        atakujacy = przeciwnik
        action=random.randint(1, 5)
    while player.hp > 0 and przeciwnik.hp > 0:
        if atakujacy == player:
            os.system("cls")
            print(f"\n{player.name} HP: {player.hp}/{player.max_hp} | {przeciwnik.name} HP: {przeciwnik.hp}/{przeciwnik.max_hp}")
            print("1. Atakuj")
            print("2. Użyj blogosławieństwa")
            print("3. Użyj przedmiotu")
            print("4. Broń się")
            print("5. Unikaj")
            print("6. Ucieczka")
            choice = input("> ").strip()
            if choice == "1":
                przeciwnik.hp -= player.damage
                print(f"Zadajesz {player.damage} obrażeń {przeciwnik.name}!")

                if przeciwnik.hp <= 0:
                    print(f"Pokonałeś {przeciwnik.name}!")
                    break

                # Przeciwnik atakuje z powrotem
                enemy_damage = (przeciwnik.strength // 5)
                player.hp -= enemy_damage
                print(f"{przeciwnik.name} zadaje Ci {enemy_damage} obrażeń!")

            elif choice == "2":
                print("Używasz blogosławieństwa!")
            elif choice == "3":
                print("Używasz przedmiotu!")
            elif choice == "4":
                print("Broń się!")
            elif choice == "5":
                print("Unikasz ataku!")
            elif choice == "6":
                print("Uciekasz z walki!")
                break
            else:
                print("Nieprawidłowy wybór, spróbuj ponownie.")
        
            atakujacy = przeciwnik
        if atakujacy == przeciwnik:
            os.system("cls")
            if przeciwnik.strength==0:
                print(f"{przeciwnik.name} stoi bezczynnie, nie zadaje obrażeń.")
                przeciwnik.hp =przeciwnik.max_hp
            else:
                os.system("cls")
                action=random.randint(1, 5)
                if action == 1:
                    enemy_damage = (przeciwnik.strength // 5)
                    player.hp -= enemy_damage
                    print(f"{przeciwnik.name} zadaje Ci {enemy_damage} obrażeń!")
                elif action == 2:
                    print(f"{przeciwnik.name} broni się!")
                elif action == 3:
                    print(f"{przeciwnik.name} unika ataku!")
            atakujacy = player
    if player.hp <= 0:
        print("Zostałeś pokonany! Game Over.")
    else:        print("Wygrałeś walkę!")