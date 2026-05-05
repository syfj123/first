#1,2

# n1=int(input("give me ur first number: "))
# n2=int(input("give me ur second number: "))

# if n1%2==0 and n2%2==0:
#     print("sum of ur numbers is: ",n1+n2)
#     sum=n1+n2
#     strsum=str(sum)
#     td=0
#     ed=0
#     for i in strsum:
#         x=int(i)
#         td+=1
#         if x%2==0:
#             ed+=1
#     if ed==td:
#         print("all digits in ur sum are even.")
# elif n1%2!=0 and n2%2!=0:
#     print("difference of ur numbers is: ",n1-n2)
# else:
#     print("product of ur numbers is: ",n1*n2)

# 3,1

for i in range(500,521):
    if i%2==0:
        print(i)
i=500

# 3,2

while i<=520:
    if i%2==0:
        print(i)
    i+=1

# rps (4)

# import random
# import time

# game=1

# while game==1:
#     opp=random.choice(['rock','paper','scissors']) # randomly picks 1 from the list
#     cont=int(input("cntinue? 1 to continue and 0 to quit: "))
#     if cont==0:
#         break
#     player=input("pick rock paper or scissors: ")
#     print("opponent chose.... ")
#     time.sleep(2)
#     print(opp,"!")
#     print("result is.....")
#     time.sleep(1)
#     if (player=="rock" and opp=="paper") or (player=="paper" and opp=="scissors") or (player=="scissors" and opp=="rock"):
#         print("you lose!")
#     elif (player=="rock" and opp=="scissors") or (player=="paper" and opp=="rock") or (player=="scissors" and opp=="paper"):
#         print("you win!")
#     elif player==opp:
#         print("tie")
#     else:
#         print("something went wrong.. please try again later!")
