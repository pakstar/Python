import random
number = random.randint(1,100)
counter = 0
numberguess = int(input("What is the number?: "))
while numberguess != number:
    numberguess = int(input("What is the number?: "))
    if numberguess > number:
        print("lower")

    if numberguess < number:
        print("higher")

    if numberguess == number:
        print("You win")
    
    counter +=1
        



if numberguess == number:
    print("Win")


print(f"You win {counter}")
