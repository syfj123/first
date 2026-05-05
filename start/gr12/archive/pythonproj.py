import random, time, os

from pythonprojclassesfuncs import *

def main():
    player=Player()
    crafts=CraftingSystem()

    while True:
        if len(player.crafted)==len(crafts.items):
            print("You crafted everything. You win!!!")
            break
        if player.energy<=0:
            print("You have no energy. You lose...")
            break

        print("")
        player.show_status()
        print("Choose: sleep, chop, craft, end")
        choice=input("> ").strip().lower()

        if choice=="sleep":
            player.sleep_action()
        elif choice=="chop":
            player.chop_action()
        elif choice=="craft":
            available=[i for i in crafts.items if i not in player.crafted]
            print("Available Resources:",player.resources)
            print("Available to craft:")
            for item in available:
                cost=crafts.items[item]
                print(item,"requires",cost,"resources")
            item=input("Item: ").strip().lower()
            if crafts.can_craft(item,player):
                crafts.craft(item,player)
                time.sleep(1)
                print("Item successfully crafted! Great job, player! Returning back to options...")
                time.sleep(2)
            else:
                print("Cannot craft, not enough resources! Returning back to options...")
                time.sleep(2)
        elif choice=="end":
            break
        else:
            print("Invalid")

        os.system("clear")

        if random.randint(1,6)==1:
            print("Uhhh.. there's something growling...")
            time.sleep(2)
            print("\nAnimal attack! \nThere are several boars, you try to run as fast as possible to escape them...")
            ok=player.attack_event()
            if not ok:
                time.sleep(2)
                print("\n\nYou failed the attack. You lose LOL :(")
                time.sleep(2)
                break
            else:
                time.sleep(1)
                print("\nYou've got through the attack, whew!")
                time.sleep(1)
                os.system("clear")

if __name__=="__main__":
    main()

