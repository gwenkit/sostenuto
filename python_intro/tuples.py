# parentheses; instead of square brackets

eggs = ('hello', 42, 0.5)
print(eggs[0], eggs[:1][0])
print(len(eggs))
# eggs[1] = 99 # TypeError: 'tuple' object does not support item assignment
# tuples are immutable; no method like `append()` or `remove()`
# 튜플을 사용하여, 해당 시퀀스가 ​​변경되는 것을 원하지 않는다는 뜻을 전달할 수 있습니다.


# trailing comma

print(type(('hello',))) # tuple
print(type(('hello' ))) # str


# List and Tuple Type Conversion

print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))


