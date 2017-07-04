import random

print(random.random())  #between 0 and 1 

print(random.randint(1,10))

print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])) #choice

suits = ['hearts','clubs','diamonds','spades']
random.shuffle(suits)

print(suits)
