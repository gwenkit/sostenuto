# regular expressions

import re


# compile, search and group

pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # qualifiers and quantifiers
match = pattern.search('My number is 123-456-7890.')
print(type(match), match.group())


# groups

pattern = re.compile(r'(\d{3})-(\d{3}-\d{4})')
match = pattern.search('My number is 123-456-7890.')
print(type(match), match.groups(), match.group(0), match.group(1), match.group(2))
area_code, main_number = match.groups() # tuple unpacking
print(area_code, main_number)

pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
match = pattern.search('My phone number is (123) 456-7890.')
print(type(match), match.groups())


# alternation operator; pipe

pattern = re.compile(r'Cat(erpillar|astrophe|ch|egory)')
match = pattern.search('Catch me if you can.')
print(type(match), match.group(), match.groups())


# returning all matches

pattern = re.compile(r'\d{3}-\d{3}-\d{4}') # has no groups
match = pattern.findall('Cell: 123-456-7890 Work: 987-654-3210')
# print(match.group(), match.groups()) # AttributeError: 'list' object has no attribute 'group'
print(type(match), match)

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') # has groups
match = pattern.findall('Cell: 123-456-7890 Work: 987-654-3210')
print(type(match), match)

pattern = re.compile(r'\d{3}')
match = pattern.findall('1234')
print(type(match), match)
# `findall()` doesn't overlap matches; 123(O), 234(X)


# character class qualifier

# vowel_pattern = re.compile(r'a|e|i|o|u|A|E|I|O|U')
vowel_pattern = re.compile(r'[aeiouAEIOU]')
match = vowel_pattern.findall('RoboCop eats BABY FOOD.')
print(type(match), match)
# e.g. [a-zA-Z0-9] will match all lowercase letters, uppercase letters, and numbers
# NOT need to escape characters inside the square brackets; e.g. `[()]` works

consonant_pattern = re.compile(r'[^aeiouAEIOU]') # negative character class
match = consonant_pattern.findall('RoboCop eats BABY FOOD.')
print(type(match), match)


# shorthand character class
# + `\d`; [0-9]
# + `\D`; [^0-9]
# + `\w`; any letter, numeric digit, or the underscore character; word
# + `\W`; any character that is not a letter, numeric digit, or the underscore character
# + `\s`; any space, tab, or newline character; space
# + `\S`; any character that is not a space, tab, or newline character

pattern = re.compile(r'\d+\s\w+') # one or more numeric digits, followed by a whitespace character, followed by one or more letter|digit|underscore characters
match = pattern.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(type(match), match)


# see(https://automatetheboringstuff.com/3e/chapter9.html#calibre_link-201)
# see(https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/)
# see(https://youtu.be/PYYfVqtcWQY)


# dot; matches JUST ONE character except for a newline

at_re = re.compile(r'.at')
match = at_re.findall('The cat in the hat sat on the flat mat.')
print(type(match), match)


# match a pattern only optionally; quantifier {0,1}

pattern = re.compile(r'42!?') # means that the pattern '!'(the exclamation mark) is optional
match = pattern.search('42!')
print(type(match), match, match.group())
match = pattern.search('42')
print(type(match), match, match.group())

pattern = re.compile(r'42?!')
match = pattern.search('42!')
print(type(match), match, match.group())
match = pattern.search('42') # None
print(type(match), match)
match = pattern.search('4!')
print(type(match), match, match.group())

pattern = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
match = pattern.search('My number is 123-456-7890')
print(type(match), match, match.group())
match = pattern.search('My number is 456-7890')
print(type(match), match, match.group())


# asterisk; zero or more; quantifier {0,}
# plus; one or more; quantifier {1,}

pattern = re.compile(r'Eggs( and spam)+')
match = pattern.search('Eggs') # None
print(type(match), match)
pattern = re.compile(r'Eggs( and spam)*')
match = pattern.search('Eggs')
print(type(match), match)
match = pattern.search('Eggs and spam and spam and spam')
print(type(match), match)


# quantifier; matching a specific number of qualifiers

pattern = re.compile(r'(Ha){3,5}') # minimum, maximum
match = pattern.search('HaHa') # None
print(type(match), match)
match = pattern.search('HaHaHa')
print(type(match), match)
match = pattern.search('HaHaHaHaHaHaHaHaHa')
print(type(match), match) # 'HaHaHaHaHa'
# greedy match; by default; in ambiguous situations, match the longest possible
pattern = re.compile(r'(Ha){3,5}?') # non-greedy; lazy match; matches the shortest string possible
match = pattern.search('HaHaHaHaHaHaHaHaHa')
print(type(match), match) # 'HaHaHa'


# dot-star; `(.*)`; match everything and anything

pattern = re.compile(r'First Name: (.*) Last Name: (.*)') # greedy mode
match = pattern.search('First Name: Al Last Name: Sweigart')
print(type(match), match, match.groups(), match.group(1), match.group(2))

pattern = re.compile(r'<.*>') # greedy mode
match = pattern.search('<To serve man> for dinner.>')
print(type(match), match, match.groups())
pattern = re.compile(r'<.*?>') # lazy mode
match = pattern.search('<To serve man> for dinner.>')
print(type(match), match, match.groups())


# including the newline characters

pattern = re.compile('.*', re.DOTALL)
match = pattern.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(type(match), match.group())


# caret symbol; start with
# dollar sign; end with

pattern = re.compile(r'^Hello')
match = pattern.search('Hello, world!')
print(type(match), match.group())
pattern = re.compile(r'\d$')
match = pattern.search('Your number is 1234')
print(type(match), match.group()) # 4
pattern = re.compile(r'\d+$')
match = pattern.search('Your number is 1234')
print(type(match), match.group()) # 1234


# word boundary

pattern = re.compile(r'\bcat.*?\b')
match = pattern.findall('The cat found a catapult catalog in the catacombs.')
print(type(match), match)

pattern = re.compile(r'\Bcat\B') # matches anything that is not a word boundary
match = pattern.findall('certificate')
print(type(match), match)
match = pattern.findall('catastrophe') # No match
print(type(match), match)
# useful for finding matches in the middle of a word


# `re.IGNORECASE` or `re.I`

pattern = re.compile(r'robocop', re.I)
match = pattern.search('RoboCop is part man, part machine, all cop.')
print(type(match), match.group())
match = pattern.search('ROBOCOP protects the innocent.')
print(type(match), match.group())
match = pattern.search('Have you seen robocop?')
print(type(match), match.group())


# substitute

pattern = re.compile(r'Agent \w+')
match = pattern.sub('CENSORED', 'Agent Alice contacted Agent Bob.') # str
print(type(match), match)
pattern = re.compile(r'Agent (\w)\w*')
match = pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
print(type(match), match)


# `re.VERBOSE`; spread the regular expression over multiple lines and use comments to label its components
# e.g.
pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # Area code
    (\s|-|\.)?  # Separator
    \d{3}  # First three digits
    (\s|-|\.)  # Separator
    \d{4}  # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})?  # Extension
    )''', re.VERBOSE)


# "bitwise or" operator
# e.g.
pattern = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)


# Humre module; for human-readable regexes

from humre import *
phone_regex_example = exactly(3, DIGIT) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)
print(phone_regex_example)
other_regex_example = one_or_more_lazy('A')
print(other_regex_example)
group_regex_example = at_least_group(3, 'A')
print(group_regex_example)


# VERBOSE example

phone_regex = group(
    optional_group(either(exactly(3, DIGIT),  # Area code
                            OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN)),
    optional(group_either(WHITESPACE, '-', PERIOD)),  # Separator
    group(exactly(3, DIGIT)),  # First three digits
    group_either(WHITESPACE, '-', PERIOD),  # Separator
    group(exactly(4, DIGIT)),  # Last four digits
    optional_group(  # Extension
        zero_or_more(WHITESPACE),
        group_either('ext', 'x', r'ext\.'),
        zero_or_more(WHITESPACE),
        group(between(2, 5, DIGIT))
    )
)
print(phone_regex)


# e.g. regex version of the `strip()` method
pattern = re.compile(r'^\s+|\s+$')
match = pattern.sub('', '   Hello,   world !        ')
print(type(match), '[' + match + ']')


