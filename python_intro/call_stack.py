# The call stack is how Python remembers where to return the execution after each function call.
# + When your program calls a function, Python creates a frame object on the top of the call stack.
# + Frame objects store the line number of the original function call
# + so that Python can remember where to return.

def a():
    print('a() starts')
    b()
    d()
    print('a() returns')


def b():
    print('b() starts')
    c()
    print('b() returns')


def c():
    print('c() starts')
    print('c() returns')


def d():
    print('d() starts')
    print('d() returns')


a()


