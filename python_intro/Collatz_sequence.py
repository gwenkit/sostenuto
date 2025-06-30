# the Collatz sequence; the simplest impossible math problem

import sys


def collatz(number):
    res = 0

    if type(number) is not int or number < 1:
        print('input must be a positive integer')
        sys.exit()

    if number % 2 == 0: # even number
        res = number // 2
    else: # odd number
        res = 3 * number + 1

    return res


user_input = input('>')
# num = 0
try:
    num = int(user_input) # global; useful
except:
    print('input must be a number')
    sys.exit()

while True:
    if num > 0:
        print(num, end=' ')

    if num == 1:
        print()
        break
    
    num = collatz(num)


# python Collatz_sequence.py


