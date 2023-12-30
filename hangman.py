import random

for i in range(10):
    number = random.choice(100)
    choice = input("What is the number")
    if (choice < number) or (choice > number):
        print("Wrong")
    else:
        print('You win')


