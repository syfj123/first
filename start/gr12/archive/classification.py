name=input("gimmey your name: ")
age=int(input("age???: "))
height=int(input("whats your height in cm: "))

if age<=4:
    class1="baby"
elif age>=5 and age<=12:
    class1="kiddo"
elif age>=13 and age<=18:
    class1="teen"
elif age>18:
    class1="fossil"

if height<=99:
    class2="🫘"
elif height>100 and height<=150:
    class2="🦐"
elif height>150 and height<=176:
    class2="🚶"
elif height>176:
    class2="🗼"

print(name+" is a "+class2+" "+class1+".")

