import random

name = input("What's up new guy, welcome to 67 RNG. What's your name?\n ")
start = input(f"Nice to meet you {name}, do you wanna play the game? \n 1 - yes \n 2 - no \n").strip()

if start == "1":
    print("Great, now let us start. Here are your stats. \n")
else:
    print("Whatever bozo.")
    exit()

class user:
    def __init__(self, name):
         self.name = name
         self.luck = 1

player1 = user(name)

auras = []
def roll():
    print("You rolled an aura")
    chance = random.randint(1, 100)
    if chance <= 50:
        print("You got an uncommon aura.")
        auras.append("Uncommon")
    elif chance in range(51, 81):
        print("You got a rare aura")
        auras.append("Rare")
    elif chance in range(81, 91):
        print("You got an epic aura")
        auras.append("Epic")
    elif chance in range(91, 95):
        print("You got a legendary aura")
        auras.append("Legendary")
    elif chance == 100:
        print("You got a Mythical aura")
        auras.append("Mythical")
    else:
        print("You got nothing lol")


def inventory():
    print("Your auras: \n")
    print(auras)

def main():
    print(f"User's Stats \n Name: {player1.name} \n Luck: {player1.luck} \n")

    while start == "1":
        inp = input("\nActions: \n Roll an aura - 1 \n Check inventory - 2 \n Exit - 3 \n")
        if inp == "1":
            roll()
        elif inp == "2":
            inventory()
        else:
            exit()
            

main()
