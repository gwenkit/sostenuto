# Detect errors, Handle them, and then continue to Run

def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))  # Prints 'Error: Invalid argument.'
                # then prints `None`
print(spam(1))


# python exception_handling.py


