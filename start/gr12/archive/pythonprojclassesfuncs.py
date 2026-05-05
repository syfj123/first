import random, time, os

class Player:
    def __init__(self):
        self.energy=random.randint(4,6)
        self.resources=0
        self.day=1
        self.crafted=[]

    def sleep_action(self):
        self.energy+=3
        self.day+=1

    def chop_action(self):
        gain=random.randint(1,4)
        self.resources+=gain
        self.energy-=2

    def attack_event(self):
        need=random.randint(3,8)
        print("This attack requires ",need," energy to survive. Can you do it, player...?")
        time.sleep(2)
        if self.energy>=need:
            loss=random.randint(2,4)
            self.energy-=loss
            self.energy+=2
            return True
        return False

    def show_status(self):
        print("Day",self.day)
        print("Energy",self.energy)
        print("Resources",self.resources)
        print("Crafted",self.crafted)

class CraftingSystem:
    def __init__(self):
        self.items={
            "shelter":random.randint(12,16),
            "bed":random.randint(8,14),
            "fire":random.randint(3,6),
            "spear":random.randint(5,7),
            "basket":random.randint(1,4)
        }

    def can_craft(self,item,player):
        if item not in self.items:
            return False
        if item in player.crafted:
            return False
        return player.resources>=self.items[item]

    def craft(self,item,player):
        cost=self.items[item]
        player.resources-=cost
        player.crafted.append(item)
