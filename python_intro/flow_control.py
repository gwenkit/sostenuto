# Components of Flow control statements
# + condition; the Boolean expression
# + clause; block of code

name = 'Tom'
if name == 'Alice':
    print('Hi, Alice.')
elif name == 'Tom':
    print('Hi, Tom.')
else:
    print('Hello, stranger.')


# The order of the `elif` statements DOES matter.
age = 3000
if age < 12:
    print('kiddo')
elif age > 90:
    print('grannie')
elif age > 1000: # never happen
    print('undead')
else:
    print('lucky')
# bad readability example


# python flow_control.py


