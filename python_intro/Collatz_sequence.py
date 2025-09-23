# the Collatz sequence; the simplest impossible math problem

import sys


def collatz(number):
    """Return the next number in the Collatz sequence."""
    if type(number) is not int or number < 1:
        print('Input must be a positive integer')
        sys.exit()

    if number % 2 == 0:  # even number
        return number // 2
    else:  # odd number
        return 3 * number + 1


user_input = input('Enter a positive integer: ')
try:
    num = int(user_input)
except ValueError:
    print('Input must be a number')
    sys.exit()

while True:
    print(num, end=' ')
    if num == 1:
        print()
        break
    num = collatz(num)


