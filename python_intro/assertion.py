# sanity checks
# should not handle `assert` statements with `try` and `except`;
# if an assert fails, program should crash!
# fail fast

ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]

ages.sort()
print(ages)
assert ages[0] <= ages[-1]

ages.reverse()
print(ages)
assert ages[0] <= ages[-1], 'message if False'


# python assertion.py


