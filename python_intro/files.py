# tested on macOS

from pathlib import Path
import os
import time


path = Path('spam', 'bacon', 'eggs')
print(type(path)) # pathlib.PosixPath
# POSIX is a set of standards for Unix-like operating systems
print(path) # spam/bacon/eggs
# 참고로, WindowsPath('spam/bacon/eggs') on Windows
print(str(path)) # spam/bacon/eggs


# the `/` operator

print( Path('spam') / 'bacon' / 'eggs' )
print( Path('spam') / Path('bacon/eggs') )
print( Path('spam') / Path('bacon', 'eggs') )
print( os.path.join('spam', 'bacon', 'eggs') ) # old style


# current working directory

print(Path.cwd())
print(os.getcwd()) # old style

backup_path = Path.cwd()
os.chdir('.')
print(Path.cwd() == backup_path)
os.chdir('..')
print(Path.cwd(), '위로(..)')
# os.chdir('/test') # e.g. FileNotFoundError: [Errno 2] No such file or directory: '/test'
os.chdir(backup_path)
print(Path.cwd())


# test WindowsPath on macOS
# e.g.
# os.makedirs('C:\\delicious\\walnut\\waffles') # old style
# created only one directory file which name is ugly; 'C/\delicious\walnut\waffles'; not expected result


# `Path.mkdir()`; new style
# e.g.
#(Path.cwd() / r'test1/test2/test3').mkdir(parents=True)


# anatomy of a filepath

print(Path.cwd().is_absolute(), Path('spam/bacon/eggs').is_absolute())
print(Path('spam/bacon/eggs').absolute())
path = Path.cwd() / r'spam/bacon/eggs.txt'
print(path)
print(path.parts) # tuple
print('anchor:', path.anchor) # str
print('drive:', path.drive) # str; part of anchor; available on Windows; e.g. 'C:'
print('parent:', path.parent) # pathlib.PosixPath
print(tuple(path.parents))
print('name:', path.name) # name = stem + suffix
print('stem:', path.stem)
print('suffix:', path.suffix)
print('root:', path.root)
print(path.root == path.parts[0], path.root == str(path.parents[-1]))
print(str(path), 'exists?', path.exists())
print(str(path), 'is dir?', path.is_dir())
print(str(path), 'is file?', path.is_file()) # False because it does not exist
print(Path.home()) # home directory
p = Path.cwd()
print(str(p), 'exists?', p.exists())
print(str(p), 'is dir?', p.is_dir())
print(str(p), 'is file?', p.is_file()) # False because it is a directory
print(str(Path.home()) == (p.parts[0] + '/'.join(p.parts[1:3])))
print(p.stat()) # `os.stat_result`
print(p.stat().st_size, 'bytes')
print(time.asctime(time.localtime(p.stat().st_mtime))) # the last time the file’s metadata was changed
print(list(p.glob('*.md'))) # glob patterns


# `Path` object methods allow only basic interactions with files

p = Path('spam.log')
print(type(p.write_text('Hello, world!'))) # characters; int
print(type(p.read_text())) # contents; str


# default `mode='r'`; read mode

readme_file = open('README.md', encoding='utf-8')
print(readme_file)
# readme_content = readme_file.read()
# print(type(readme_content)) # str
readme_lines = readme_file.readlines()
print(readme_lines) # list
readme_file.close()


# + write mode; write plaintext mode
# + append mode; append plaintext mode

bacon_file = open('bacon.log', 'w', encoding='utf-8')
bacon_file.write('Hello, world!\n') # return int
bacon_file.close()

bacon_file = open('bacon.log', 'a', encoding='utf-8')
bacon_file.write('Bacon is not a vegetable.\n') # return int
bacon_file.close()


# with statement

with open('bacon.log', 'a', encoding='utf-8') as bacon_file:
    bacon_file.write('Hello, world!')
with open('bacon.log', encoding='utf-8') as bacon_file:
    bacon_content = bacon_file.read()
# no calls to `close()` at all
# because the `with` statement automatically calls it when the program execution leaves the block
# The `with` statement knows to do this based on the context manager it obtains from the `open()` function

print(bacon_file)
print(bacon_content)


# shelve; binary shelf files; kind of database

import shelve


shelf_file = shelve.open('mydata.log')
shelf_file['cats'] = ['Zophie', 'Pooka', 'Simon']
shelf_file['pi'] = 3.14
shelf_file.close()
# try(`strings mydata`) on shell

shelf_file = shelve.open('mydata.log')
print(type(shelf_file))
print(list(shelf_file.keys()))
print(list(shelf_file.values()))
print(shelf_file['cats'])
shelf_file.close()


# python files.py


