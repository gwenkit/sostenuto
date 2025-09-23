# A variable must be local or global;
# it cannot be both local and global.

def test_error():
    print(eggs) # UnboundLocalError: local variable 'eggs' referenced before assignment
                # "binding" is another way of saying "assigning"
    eggs = 'spam local'
# test_error()


# to modify a global variable from within a function, use the `global` statement

def spam():
    global eggs
    eggs = 'spam' # No local 'eggs' variable is ever created.

eggs = 'global'
spam()
print(eggs) # Prints 'spam'


# global variable example

import random


random_number = random.randint(1, 6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    # But this 'random_number' is a global variable
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())


