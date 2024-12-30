#using random module

import random

coin = random.choice(["heads","tails"])
print(coin)

# use of from

from random import choice
coin = choice(["heads","tails"])
print(coin)