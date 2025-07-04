# indexes and slices

greeting = 'Hello, world!'
captured_slice = greeting[7:-1]
print(captured_slice)


# raw string

print('Hello...\n\n...world!')  # without a raw string
print(r'Hello...\n\n...world!')  # with a raw string


# multiline strings

print('''Dear Alice,

Can you feed Eve's cat this weekend?

Sincerely,
Bob''')


def say_hello():
    """This function prints hello.
    It does not return anything."""
    print('Hello!')

say_hello()


# f-string

name = 'Al'
age = 4000
print(f'My name is {name}. I am {age} years old.')
print(f'In ten years I will be {age + 10}')
print(f'{{name}}') # double curly brackets are literal curly brackets.


# string interpolation; old

print('My name is %s. I am %s years old.' % (name, age))


# method `format()`

print('My name is {}. I am {} years old.'.format(name, age))
print('{1} years ago, {0} was born and named {0}.'.format(name, age))


# method `upper()`, `lower()`, `isupper()`, `islower()`

spam = 'Hello, world!'
print(spam.islower(), spam.isupper())
spam = spam.upper()
print(spam, spam.islower(), spam.isupper())
spam = spam.lower()
print(spam, spam.islower(), spam.isupper())
print('Hello'.upper().lower().upper())


# method `isalpha()`, `isalnum()`, `istitle()`, `isspace()`, `isdecimal()`

print('hello'.isalpha(), 'hello'.isalnum())
print('Hello, world!'.istitle(), 'Hello, World!'.istitle())
print('01'.isdecimal(), '\t\r\n'.isspace())


# method `startwith()`, `endwith()`

print('Hello!'.startswith('h'))
print('hello!'.endswith('o'))
print('hello'.startswith('hello'), 'hello'.endswith('hello'))


# method `join()`, `split()`

print(', '.join(['a', 'b', 'c']))
print('My name is Simon'.split())
print('My name is Simon'.split('m'))


lines = '''Dear Alice,
There is a milk bottle in the fridge
that is labeled "Milk Experiment."

Please do not drink it.
Sincerely,
Bob'''.split('\n')
print(len(lines)) # 7


# method `rjust()`, `ljust()`

print('Hello'.rjust(10))
print('Hello'.rjust(20))
print('Hello, World'.rjust(20))
print('Hello'.rjust(20, '*'))
print('$' + 'Hello'.ljust(18) + '$')
print('Hello'.ljust(20, '-'))
print('Hello'.center(20, '='))


# method `strip()`, `lstrip()`, `rstrip()`

spam = '    Hello, World    '
print('$' + spam.strip() + '$')
print('$' + spam.rstrip() + '$')
print('$' + spam.lstrip() + '$')

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # the order of the characters in the string passed to `strip()` doesn't matter


# utf-8

print(ord('A') < ord('B')) # 65 < 66
print(chr(ord('A') + 1))


# show all methods

print(dir(str))


# example

table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]

def print_table():
    table = []
    max_string_len_arr = [0, 0, 0,]

    for i in range(3):
        for j in range(4):
            if max_string_len_arr[i] < len(table_data[i][j]):
                max_string_len_arr[i] = len(table_data[i][j])
        table += table_data[i]
    # print(max_string_len_arr)

    for i in range(4):
        print(
            table[i].rjust(max_string_len_arr[0]),
            table[i+4].rjust(max_string_len_arr[1]),
            table[i+8].rjust(max_string_len_arr[2]),
        )

print_table()


# python strings.py


