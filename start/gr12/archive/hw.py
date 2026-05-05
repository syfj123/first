def pos_or_neg_or_zero():
    num=int(input("give me a number: "))
    if num>0:
        print("yo number psitivie\n")
    elif num<0:
        print("number is negative\n")
    elif num==0:
        print("number is zero pal\n")

def fah_to_cel():
    fah=float(input("give me a temperature in fahrenheit: "))
    cel=str((fah-32)/1.8)
    kel=str(float(cel)+273.15)
    print("that temperature in celsius isssss: "+cel+", and that temperature to kelvin isss: "+kel+"\n")

def leap_year_checker():
    year=int(input("give me a year (e.g. 2025): "))
    if (year%4==0 and year%100!=0) or year%400==0:
        print("leap year yeahhhhh\n")
    else:
        print("not leap year pal :(\n")

def sum_series():
    num=int(input("give me a number, positive: "))
    out=str(int((num/2)*(num+1)))
    print("sum of series is: "+out+"\n")

while True:
    choice=int(input("choose what you wanna do:\n1. pos/neg/zero detector\n2. fahrenheit to celsius converter\n3. leap year checker\n4. sum of series\n5. exit\n\nenter number: "))
    if choice==1:
        pos_or_neg_or_zero()
    elif choice==2:
        fah_to_cel()
    elif choice==3:
        leap_year_checker()
    elif choice==4:
        sum_series()
    elif choice==5:
        print("bye pal")
        break
    else:
        print("invalid choice pal")
