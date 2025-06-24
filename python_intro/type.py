# int
print(type(-1))

# float
print(type(3.14))

# str
print(type('Alice' * 5))


# strings are text, while integers and floats are numbers.

print(42 == '42')
# False

print(42 == 42.0)
# True

print(42.0 == 0042.000)
# True

print(3.1 == round(3.14, 1))
# True


# banker's rounding
print(round(2.5), round(3.5), round(4.5), round(5.5))
# 2 4 4 6


# Unicode code point; character
ord_A = ord('A')
chr_A = chr(ord_A)
print(ord_A, chr_A, bin(ord_A), hex(ord_A))
# 65 A 0b1000001 0x41


# Boolean operator

print(False and False)
# False

print(not not not not True)
# True

# after any math and comparison operators evaluate,
# then order of `not`, `and`, and finally `or`
print(not True or not False and not not True and 2 + 2 == 2 * 2)
# True


# python type.py


