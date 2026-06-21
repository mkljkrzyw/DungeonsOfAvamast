import random
class rapax:
    name = "Rapax"
    hp = 800
    max_hp = 800
    strength = 50
    dexterity = 10
    intelligence = 10
    damage = 60
    defense = 10
    currentdefense=defense
class kukla_treningowa:
    name = "Kukła treningowa"
    hp = 9999999
    max_hp = 9999999
    strength = 0
    dexterity = 0
    intelligence = 0
    damage = 0
    defense = 10
    currentdefense=defense
    exp=0
class test:
    name = "Test"
    hp = 100
    max_hp = 100
    strength = 10
    dexterity = 10
    intelligence = 10
    damage = 10
    defense = 10
    currentdefense=defense
    exp=0
class dopler:
    name="Potwór przypominający smutną kobietę"
    hp=50
    max_hp=50
    strength = 5
    dexterity = 5
    intelligence = 5
    damage = 5
    defense = 5
    currentdefense=defense
    exp=30
    gold=20
class bandyta:
    name="Bandyta"
    max_hp=random.randint(75, 85)
    hp=random.randint(max_hp-10, max_hp)
    strength = random.randint(8, 12)
    dexterity = random.randint(8, 12)
    intelligence = 5
    damage = random.randint(strength, strength+3)
    defense = 10
    currentdefense=defense
    exp=random.randint(10, 30)
    gold=random.randint(0, 25)
class omerio:
    name="Omerio"
    hp=150
    max_hp=150
    strength = 15
    dexterity = 15
    intelligence = 15
    damage = 20
    defense = 10
    currentdefense=defense
    exp=70
class darn:
    name="Darn"
    hp=100
    max_hp=100
    strength = 10
    dexterity = 10
    intelligence = 10
    damage = 15
    defense = 10
    currentdefense=defense
    exp=30