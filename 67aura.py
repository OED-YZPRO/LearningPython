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
         self.money = 0
         self.potions = 0

player1 = user(name)

aas = ['uncommon', 'rare', 'epic', 'legendary', 'mythical']

auras = []
def roll():
    print("You rolled an aura")
    chance = random.randint(1, 100)
    if chance <= 50:
        print(f"You got an {aas[0]} aura.")
        auras.append(aas[0])
    elif chance in range(51, 81): 
        print(f"You got an {aas[1]} aura.")
        auras.append(aas[1])
    elif chance in range(81, 91):
        print(f"You got an {aas[2]} aura.")
        auras.append(aas[2])
    elif chance in range(91, 95):
       print(f"You got an {aas[3]} aura.")
        auras.append(aas[3])
    elif chance == 100:
      print(f"You got an {aas[4]} aura.")
        auras.append(aas[4])
    else:
        print("You got nothing lol")
        
def shop():
    while do /= '3':
        do = input('What do you want to do? \n buy potions - 1 \n sell auras - 2 \n exit the shop - 3 \n')
        if do == "1":
            if player1.money >= 50:
                player1.money -= 50
            else:
                print("You don't have enough money")
        
    
    


def inventory():
    print("Your auras: \n")
    print(auras)

def main():
    print(f"User's Stats \n Name: {player1.name} \n Luck: {player1.luck} \n")

    while start == "1":
        inp = input("\nActions: \n Roll an aura - 1                                                 \n Check inventory - 2 \n Check stats - 3 \n Shop - 4 \n 6 - drink a potion \n Exit - 5 \n")
        if inp == "1":
            roll()
        elif inp == "2":
            inventory()
        elif inp == "3":
            print(f"User's Stats \n Name: {player1.name} \n Luck: {player1.luck} \n")
        elif inp == "4":
            start = 0
            shop()
        else:
            exit()
            

main()







