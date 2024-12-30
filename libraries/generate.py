#using random module

import random

coin = random.choice(["heads","tails"])
print(coin)

# use of from

from random import choice
coin = choice(["heads","tails"])
print(coin)


#how get a random no between a range example [1,10]
'''using random.randint(1,10)'''

import random

number = random.randint(1,10)
print(number)


#How to shuffle elements given in our list (eg. list of cards)

import random

cards = ["King", "Queen", "Jack"]
random.shuffle(cards)
for card in cards:
    print(card)