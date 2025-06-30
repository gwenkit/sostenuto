# for loop

print('Hello!')
for i in range(5):
    print('On this iteration, i is set to ' + str(i))
print('Goodbye!')
print()


# though not clever as Carl Friedrich Gauss
total = 0
for num in range(101):
    # range(101)
    # + start with 0
    # + UP TO BUT NOT INCLUDING 101
    # called as a "closed, open" format
    total = total + num
print(total)
print()


print("range(12, 16)")
for i in range(12, 16):
    print(i)
print()

print("range(0, 10, 2)")
for i in range(0, 10, 2):
    print(i)
print()

print("range(5, -1, -1)")
for i in range(5, -1, -1):
    print(i)
print()

print("range(5, -1, -2)")
for i in range(5, -1, -2):
    print(i)
print()


# Guess the Number

import random


secret_number = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guesses_taken in range(1, 7):
    print('Take a guess.')
    guess = int(input('>'))

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break  # This condition is the correct guess!

if guess == secret_number:
    print('Good job! You got it in ' + str(guesses_taken) + ' guesses!')
else:
    print('Nope. The number was ' + str(secret_number))


# test `KeyboardInterrupt`

# while True:
#     print('Please press CTRL-C')


# python loops.py


