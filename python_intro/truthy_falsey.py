# truthy

print(bool(1))
print(bool(00000000.00000001))
print(bool(' '))


# falsey

print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(None))


# easier to read with falsey
name = ''
if not name:
    print("not name")
if not name != '':
    print("not name != ''")


