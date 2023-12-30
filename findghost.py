import random

ghost_door = random.randint(1,3)
print("Three doors ahead. A ghoast behind one. Which door you open?")
guess = int(input("1,2 or 3: "))

while guess > 1 or guess > 3:
    print("Wrong number")
    guess = int(input("1,2,3?"))


if ghost_door != guess:  
     print("No ghost. You win!")
else:
     print("Ghost! Game over.")

