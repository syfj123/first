import time, os
money = 3
seeds = 0
plants = [] #2d array
# e.g. plants=


def show_farm():
    '''print out the status of each seed'''
    pass

def next_day():
    

def water():
    '''Reset water level of plant(s)'''
    pass

#TODO harvest, sell crops, shop

def show_menu():
    print("1. Print stats")
    print("2. Plant a seed")


game = 1

while game:
    show_menu()
    user = int(input("Option Select: "))
    if user==1:
        print("Your current money: ",money,"\nYour current seeds: ",seeds,"\nYour current plants: ",plants)
    elif user==2:
        newplants=[]
        newplants.append("name")
        newplants.append(100) # water level
        newplants.append(0) # age
        plants.append(newplants)

    wait=input("Press enter to continue... ")

    next_day()
    os.system("clear")

