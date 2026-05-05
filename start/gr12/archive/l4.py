import os, time

arg=True
pets=[]

while arg:
    os.system("clear")
    print("Loading...")
    time.sleep(3)
    print("Welcome\nOptions:\n1. Add a pet\n2. Remove a pet\nType end to exit program.")
    time.sleep(3)
    user=input("Option select: ")
    if user=="1" or user=="1.":
        new=input("What pet do you want to add to database?: ")
        print("Adding your pet!...")
        time.sleep(3)
        pets.append(new)
        print("Your pet, ",new,", has been added to database!")
        print("Current pets: ",pets,".")
    elif user=="2" or user=="2.":
        remove=1
        print(pets)
        while remove:
            del1=input("Who do you want to kill brutally?: ")
            if del1 in pets:
                print("Removing your pet!...")
                time.sleep(3)
                pets.remove(del1)
                remove=0
            else:
                print("This pet ain't there gang.")
        print(pets)
    elif user=="end":
        arg=False
        print(pets)
