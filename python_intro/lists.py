# the sequence data types contain multiple values in an ordered sequence
# + lists
# + tuples
# + strings

print([])
print(list())


spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)
print(len(spam))


# index; integer

print(spam[0], spam[-1], spam[-2])
print(['cat', 'bat', 'rat', 'elephant'][3])
del spam[2]
print(spam) # ['cat', 'bat', 'elephant']
del spam[2]
print(spam) # ['cat', 'bat']
# spam[2] # IndexError: list index out of range


# lists themselves can contain other lists;
# useful to arrange data into hierarchical structures.

spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
print(spam[1][3])
spam[-1] = 12345 # lists are mutable
print(spam)
# spam[1][3] # TypeError: 'int' object is not subscriptable


# slice

spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[0:-1])
print(spam[:2]) # using the beginning of the list
print(spam[1:]) # using the length of the list
print(spam[:])
print(spam[0:1000]) # no error


# concatenation and replication

print([1, 2, 3] + ['A', 'B', 'C']) # concatenation
print(['X', 'Y', 'Z'] * 3) # replication
spam = [1, 2, 3]
spam += ['A', 'B', 'C'] # augmented assignment operator; concatenation
print(spam)
spam *= 3 # augmented assignment operator; replication
print(spam)


# `for` loops

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

for i in range(len(supplies)):
    print(i, supplies[i])

for index, item in enumerate(supplies): # using unpacking
    print(index, item)


# in, not in

print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
print('cat' not in ['hello', 'hi', 'howdy', 'heyas'])


# unpacking; multiple assignment

cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
# size, color, disposition, name = cat # ValueError: not enough values to unpack


# truthy, falsey

print(bool(['']), bool([0]), bool([0,]), bool([]))


# function vs. method
# + e.g. index(spam, 'hello'); function for spam
# + e.g. spam.index('hello'); method of spam

spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Zophie'))
print(spam.index('Pooka')) # returns the index of its first appearance
# spam.index('Zophie Zophie') # ValueError: 'Zophie Zophie' is not in list
spam.append('moose') # returns `None`
print(spam)
spam.insert(1, 'chicken') # returns `None`
print(spam)
spam.remove('Pooka') # removes only the first instance and returns `None`
print(spam)
# spam.remove('bat') # ValueError: list.remove(x): x not in list
# The `del` statement is useful when you know the index of the value you want to remove from the list,
# while the `remove()` method is useful when you know the value itself.
spam.sort() # sorts the list in place and returns `None`
print(spam)
# spam.reverse()
spam.sort(reverse=True)
print(spam)
# ASCIIbetical order; NOT alphabetical order
spam.sort(key=str.lower) # in regular alphabetical order
print(spam)
# [1, 3, 2, 4, 'Alice', 'Bob'].sort() # TypeError: '<' not supported between instances of 'str' and 'int'

print(dir(spam)) # find methods of spam


# random example

import random


pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))
random.shuffle(pets)
print(pets)
random.shuffle(pets)
print(pets)
random.shuffle(pets)
print(pets)
# `random.shuffle` function modifies the list in place, rather than returning a new list.


# strings
name = 'Gwen'
print(name[0], name[-2])
print(name[0:9]) # no error
print(len(name))
print('we' in name, 'g' in name, 'p' not in name)
for c in name:
    print('* * * ' + c + ' * * *')
print(list('hello')) # str to list

# BUT a string is immutable!
# name[2] = 'a' # TypeError: 'str' object does not support item assignment
name = 'Zophie a cat'
new_name = name[:7] + 'the' + name[8:]
print(new_name)


# references

spam = [0, 1, 2, 3]
eggs = spam # reference; not copied
eggs[1] = 'Hello!'
print(spam) # [0, 'Hello!', 2, 3]
print(eggs) # [0, 'Hello!', 2, 3]
spam = 1
eggs = spam
spam = 10
print(spam) # 10
print(eggs) # 1
# In Python,
# + variables never contain values. They contain only references to values.
# + the `=` assignment operator copies only references. It never copies values.
# + lists contain references to values rather than values themselves.


# arguments passing reference

def eggs(some_parameter):
    some_parameter.append('Hello') # it directly modifies the list in place

spam = [1, 2, 3]
eggs(spam)
print(spam)  # [1, 2, 3, 'Hello']


# `copy.copy()`, `copy.deepcopy()`
# to work without modifying the original list

import copy


spam = ['A', 'B', 'C']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
print(cheese)
# The copy.deepcopy() function will copy these inner lists as well.


# python lists.py


