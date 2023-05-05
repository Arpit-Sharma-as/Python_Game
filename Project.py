import random
# rock paper scissors

def gamewin(comp , you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True   

    elif comp == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False 

    elif comp == 'g':
        if you == 'w':
            return True
        elif you == 's':
            return False          

print("comp 1 turn: Snake(s) water(w) or Gun(g)?")
randNo = random.randint(1, 3)


if randNo == 1:
    comp = 's'

elif randNo == 2:
    comp = "w"

elif randNo == 3:
    comp = "w"

you = input("Player's 2 turn: Snake(s) water(w) or Gun(g)?")
a = gamewin(comp , you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("you win!")

else:
    print("you loose")        