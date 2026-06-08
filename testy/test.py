import os

def help():
    print('''
Dungeons of Avamast
=================
Commands:
    go [direction]
    get [item]
    inventory 
    help
''')
inventory =[]
currentRoom = "Bedroom"
rooms = {
    "Bedroom": {
        "west": "Hallway",
        "item": "key"
    },
    "Hallway": {
        "east": "Bedroom"
    }
    }




help()
while True:
    print("You are in the " + currentRoom)
    directions = rooms[currentRoom]
    print(directions)
    turn=input(">")
    os.system("cls")
    turn = turn.split(" ",1)
    if turn[0]=="get":
        if turn[1]==rooms[currentRoom]["item"]:
            inventory.append(turn[1])
            rooms[currentRoom].pop("item")
            print("You got the " + turn[1])
        else:
            print("There is no " + turn[1] + " here")
    elif turn[0]=="go":
        if turn[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][turn[1]]
        else:
            print("You can't go that way")
    elif turn[0]=="inventory":
        print("Inventory: " + str(inventory))
    elif turn[0]=="help":
        help()
    

