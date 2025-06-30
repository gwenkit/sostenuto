# example(standard library)

import random, sys, os, math


for i in range(5):
    print(random.randint(1, 10))

print(math.pi)

while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        print('Bye!')
        sys.exit()
    print(os.name)


# python importing_modules.py


