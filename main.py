# number gussing program

import random

comp = random.randint(1,100)

attempt = 0

user = int(input("Enter a number to guess: "))

while user != comp:
    attempt +=1

    if comp > user:
        print("U've entered low, Better luck next time..")
        user= int(input("Try again... "))  

    elif comp < user:
        print("U've entered high, Better luck next time..")
        user= int(input("Try again... "))
  
if comp == user:
    attempt +=1
    print(f"Congratulation,, U entered correctly in attempt-{attempt} ")


       