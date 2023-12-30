import random
from tkinter import Y
adjectives = ['wet', 'fat', 'red', 'brave', 'yellow', 'white', 'green', 'purple' ]
nouns = ['apple ', 'ball', ' toaster', 'd uck']
special_symbols = ['!', '#', "$", '%', '&', '*', '+', '?', '@']



for i in range(3):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        special_symbol = random.choice(special_symbols)


        password = adjective +  noun +  special_symbol

        print('Your password is ', password)


        response = input("Would you like another password (y/n)")
        if response == 'n':
            break
        else:
            if response == 'y':
                continue
        
           

pass_add = input("Would you like to add noun,verb or special symbol? (y/n)")
if pass_add == 'y':
  choice_add = input("Choose (a,n,s)")
if choice_add == 'a':





#  text = 'Georg Rusev Dimitrov'
#     names = text.split('')
#     print(names)
