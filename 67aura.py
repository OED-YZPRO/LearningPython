import random

name = input("What's up new guy, welcome to 67 RNG. What's your name?\n ")
start = input(f"Nice to meet you {name}, do you wanna play the game? \n 1 - yes \n 2 - no \n").strip()

if start == "1":
    print("Great, now let us start. \n")
elif start == '2':
    print("Whatever bozo.")
    exit()
    
class user:
    def __init__(self, name):
         self.name = name
         self.luck = 1
         self.money = 0
         self.potions = 1

player1 = user(name)

aas = ['uncommon', 'rare', 'epic', 'legendary', 'mythical']

auras = []

c = 1

def roll():
    print("You rolled an aura")
    chance = random.randint(c, 100)
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
    global start
    
    do = ''
    while do != '3':
        do = input('What do you want to do? \n 1 - buy potions \n 2 - sell auras \n 3 - exit the shop \n')
        if do == "1":
            if player1.money >= 50:
                player1.money -= 50
                player1.potions += 1
            else:
                print("You don't have enough money")
        elif do == "2":
            print(aas)
            sold = input('How many auras are you going to sell?')
        elif do == '3':
            start = "1"
        else:
            pass
            
            
            
        
    
    
def inventory():
    print("Your auras: \n")
    print(auras)

stats = (f"User's Stats \n Name: {player1.name} \n Luck: {player1.luck} \n Money: {player1      .money} \n Luck Potions: {player1.potions}")

def main():
    global start
    global c
    print(start)

    while start == "1":
        inp = input("\nActions: \n 1 - Roll an aura                                                 \n 2 - Check inventory \n 3 - Check stats \n 4 - Shop                          \n 5 - drink a potion \n 6 - Exit \n")
        if inp == "1":
            roll()
        elif inp == "2":
            inventory()
        elif inp == "3":
            print(stats)
        elif inp == "4":
            start = "0"
            shop()
        elif inp == "5":
            if player1.potions == 0:
                print("you don't have any potions")
            else:
                player1.potions -= 1
                c += 5
        elif inp == '6':
            exit()
        else:
            pass
            

main()
