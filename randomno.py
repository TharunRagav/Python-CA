import random

data = list("ABCDEFGH")

print(random.choice(data))

print(random.shuffle(data))

print(random.randint(1, 100))
#will change everytime without seed 

random.seed(1)
print(random.randint(1, 100))

print(random.randrange(1, 100, 5))
#random.randrange(start, stop, step)
