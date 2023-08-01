import random
n=random.randint(1,3)
ctr=0
while ctr<5:
    guess=int(input("Guess a number in range from 1to 2:"))
    if guess==n:
        print("you win!!    :) ")
        break
    else:
        ctr+=1
if not ctr<5:
    print("You lose  :( \n The number was",n)
