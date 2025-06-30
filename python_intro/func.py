# major purpose of functions:
# + to group code that gets executed multiple times
# + to avoid duplicating code

def hello():
    print('Hello!')


# parameters are variables that contain arguments.
def hello_to(name):
    if not name:
        name = 'nobody'
        
    print('Hello,', name + '!')


hello()
hello()
hello_to('')
hello_to('Gwen') # The string 'Gwen' is an argument, the argument 'Gwen' is assigned to the `name` parameter.


# Function Returns

spam = print('Hello!')
print(None == spam)
# Behind the scenes,
# Python adds `return None` to the end of any function definition with no `return` statement
# or if there is a return statement without a value; just the return keyword by itself


import random


def get_answer(answer_number):
    # Returns a fortune answer based on what int answer_number is, 1 to 9
    if answer_number == 1:
        return 'It is certain'
    elif answer_number == 2:
        return 'It is decidedly so'
    elif answer_number == 3:
        return 'Yes'
    elif answer_number == 4:
        return 'Reply hazy try again'
    elif answer_number == 5:
        return 'Ask again later'
    elif answer_number == 6:
        return 'Concentrate and ask again'
    elif answer_number == 7:
        return 'My reply is no'
    elif answer_number == 8:
        return 'Outlook not so good'
    elif answer_number == 9:
        return 'Very doubtful'

print(get_answer(random.randint(1, 9)))
# r = random.randint(1, 9)
# fortune = get_answer(r)
# print(fortune)


# named parameter

print('Hello', end='')
print('World')

print('cats', 'dogs', 'mice', sep=',')


# python func.py


