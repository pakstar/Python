import random

numbers = []
multi = []

for i in range(20):
    number = random.randint(1,100)
    numbers.append(number)
    if number % 5 == 0:
        multi.append(number)


        result = 1
        for number in multi:
           result = result*number

print(result)