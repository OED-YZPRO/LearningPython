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


uncommon = 0
rare = 0
epic = 0
legendary = 0
mythical = 0

auras = []

def roll():
    global uncommon
    global rare
    global epic
    global legendary
    global mythical
    
    print("You rolled an aura")
    chance = random.randint(player1.luck, 100)
    if chance <= 50:
        print(f"You got an uncommon aura.")
        uncommon += 1
    elif chance in range(51, 81): 
        print(f"You got an rare aura.")
        rare += 1
    elif chance in range(81, 91):
        print(f"You got an epic aura.")
        epic += 1
    elif chance in range(91, 95):
        print(f"You got an legendary aura.")
        legendary += 1
    elif chance == 100:
        print(f"You got an mythical aura.")
        mythical += 1
    else:
        print("You got nothing lol")
        
    
def inventory():
    global auras
    auras = [f'uncommon - {uncommon}', f'rare - {rare}', 
         f'epic - {epic}', f'legendary - {legendary}',
         f'mythical - {mythical}']
         
    print("Your auras: \n")
    print(auras)
    
def shop():
    global start
    global auras
    global uncommon
    global rare
    global epic
    global legendary
    global mythic
    auras = [f'uncommon - {uncommon}', f'rare - {rare}', 
         f'epic - {epic}', f'legendary - {legendary}',
         f'mythical - {mythical}']
    
    do = ''
    while do != '3':
        do = input('What do you want to do? \n 1 - buy potions \n 2 - sell auras \n 3 - exit the shop \n')
        if do == "1":
            if player1.money >= 50:
                player1.money -= 50
                player1.potions += 1
            else:
                print("You don't have enough money \n")
        elif do == "2":
            print(auras)
            sold = input('\nWhat aura are you going to sell?\n')
            if sold != '':
                quantity = int(input('\nHow many?\n'))
                if quantity > sold or sold == 0:
                    print("You don't have that many auras.")
                else:
                    if sold == 'mythical':
                        player1.money += 50 * quantity
                        mythical -= 1
                    elif sold  == 'legendary':
                        player1.money += 20 * quantity
                        legendary -= 1
                    elif sold  == 'epic':
                        player1.money += 10 * quantity
                        epic -= 1
                    elif sold  == 'rare':
                        player1.money += 5 * quantity
                        rare -= 1
                    elif sold  == 'uncommon':
                        player1.money += 1 * quantity
                        uncommon -= 1
            else:
                pass
                print(f"You now have {player1.money} coins.")
        elif do == '3':
            start = "1"
        else:
            pass
            

def main():
    global start
    
    while start == "1":
        inp = input("\nActions: \n 1 - Roll an aura                                                 \n 2 - Check inventory \n 3 - Check stats \n 4 - Shop                          \n 5 - drink a potion \n 6 - Exit \n")
        if inp == "1":
            roll()
        elif inp == "2":
            inventory()
        elif inp == "3":
            stats = (f"User's Stats \n Name: {player1.name} \n Luck: {player1.luck} \n Money: {player1.money} \n Luck Potions: {player1.potions}")
            print(stats)
        elif inp == "4":
            start = "0"
            shop()
        elif inp == "5":
            if player1.potions == 0:
                print("you don't have any potions")
            else:
                player1.potions -= 1
                player1.luck += 5
        elif inp == '6':
            exit()
        else:
            pass
            

main()
