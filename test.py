import random

x,y = random.randint(-1000,1000),random.randint(-1000,1000)

i = 1
if x in range(-500,500) and y in range(-500,500):
    i = 0
    x+= random.randint(-1,1) * random.random()
    y+= random.randint(-1,1) * random.random()
while (x not in range(-500,500) and y not in range(-500,500)):
    print(x,y)
    if x not in range(-500,500):
        if x > 0:
            x-= random.randint(1,20)
        else:
            x+= random.randint(1,20)
    if y not in range(-500,500):
        if y > 0:
            y-= random.randint(1,20)
        else:
            y+= random.randint(1,20)

print()
print(x,y)