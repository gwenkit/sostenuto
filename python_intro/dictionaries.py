# mutable collection
# + key-value pair
# + curly brackets

print({})
print(dict())


my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print(my_cat['color'])

spam = {12345: 'Luggage Combination', 42: 'The Answer'} # use integer values as keys
print(spam[12345])
# spam[0] # KeyError: 0

print(['cats', 'dogs', 'moose'] == ['cats', 'dogs', 'moose'])
print(['cats', 'dogs', 'moose'] == ['dogs', 'moose', 'cats'])
print({'name': 'Zophie', 'species': 'cat', 'age': '8'} == {'species': 'cat', 'age': '8', 'name': 'Zophie'})
# NOT a sequence data type; can’t be sliced


# method; keys(), values(), items()

spam = {'color': 'red', 'age': 42}

print(type(spam.keys()))
print(type(spam.values()))
print(type(spam.items()))

for k in spam.keys(): # a list-like `dict_keys`; NOT a `list`
    print(k)
print(list(spam.keys())) # got a `list`

for v in spam.values(): # a list-like `dict_values`; NOT a `list`
    print(v)
print(list(spam.values())) # got a `list`

for item in spam.items(): # `dict_items`; tuples
    print(item)
for k, v in spam.items(): # unpacking tuples
    print(k, v)

print('color' in spam.keys())
print('age' not in spam.keys())
print('red' in spam.values())
print('color' in spam) # 키의 존재 여부


# method; get(), setdefault()

picnic_items = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')
# .get(key to retrieve, fallback value)

spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'
spam.setdefault('color', 'black') # returns 'black'
print(spam)
spam.setdefault('color', 'white') # Does nothing and returns 'black'; not 'white'
print(spam)


# character count example

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)


# data structure, data model example

all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}
print(all_guests)
from pprint import pprint
pprint(all_guests, indent=4)

def total_brought(guests, item):
    num_brought = 0
    for k, v in guests.items():
        num_brought = num_brought + v.get(item, 0)
    return num_brought

print('Number of things being brought:')
print(' - Apples         ' + str(total_brought(all_guests, 'apples')))
print(' - Cups           ' + str(total_brought(all_guests, 'cups')))
print(' - Cakes          ' + str(total_brought(all_guests, 'cakes')))
print(' - Ham Sandwiches ' + str(total_brought(all_guests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(total_brought(all_guests, 'apple pies')))


