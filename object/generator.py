import os
os.system('cls')
# introdução às Generator functions in python // intro to Generator Functions in python
# generator = (n for n in range(1000))

def genearator(n=0, maximum = 10):
    while True:
        yield n 
        n += 1
        
        if n > maximum:
            return

gen = genearator(maximum=8)
for n in gen:
    print(n)