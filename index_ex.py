import random

names = ['Neha', 'Lee', 'Sam' ]
verbs = ['buys', 'rides', 'kicks']
nouns = ['lion', 'bicycle', 'plane']
 

index = random.randint(0,len(names))
name = names[index]



index = random.randint(0,len(verbs))
verb = verbs[index]

index = random.randint(0,len(nouns))
noun = nouns[index]


print(f'{names} {verbs} {nouns}')