# tested on macOS(Visual Studio Code)
# copy, move, rename, and delete files

import os
import shutil
import zipfile
from pathlib import Path
import send2trash


# ready test example

# h = Path.home()
h = Path.cwd()
(h / 'spam').mkdir(exist_ok=True)
(h / 'spam2').mkdir(exist_ok=True)
with open(h / 'spam/file1.log', 'w', encoding='utf-8') as file:
    file.write('Hello\n')


# copy
# + Both source and destination can be strings or Path objects.
# + If destination is a filename, it will be used as the new name of the copied file.
# + If destination is a folder, the file will be copied to that folder with its original name.
# + This function returns the path of the copied file.

path_source = h / 'spam/file1.log'
path_destination = h / 'spam/file2.log'
shutil.copy(path_source, path_destination)
assert Path(path_source).read_text() == Path(path_destination).read_text()

path_destination = h / 'spam2'
copied = shutil.copy(path_source, path_destination)
print(copied, Path(copied).read_text())
# shutil.copytree(h / 'spam', h / 'spam3') # FileExistsError if the directory 'spam3' exists


# move or rename

moved = shutil.move(copied, path_destination / 'renamed_after_copied.log')
print(moved, Path(moved).read_text())


# delete; remove

for filename in (h / 'spam').glob('*.log'):
    # os.unlink(filename)
    print('Deleting', filename)
# This is called a "dry run".

send2trash.send2trash([h / 'spam', h / 'spam2'])
# send2trash.send2trash(h / 'spam3')


# list

dir_list1 = os.listdir(h)
print(type(dir_list1)) # <class 'list'>
print(dir_list1) # list of str

dir_list2 = h.iterdir()
print(type(dir_list2)) # <class 'generator'>
print(list(dir_list2)) # list of PosixPath


# walk

for folder_name, subfolders, filenames in os.walk(h / 'python_intro'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)

    print('')
# The `os.walk()` function doesn’t change the current working directory of the program.


# archive; compress and extract

# ready test example

(h / 'spam').mkdir(exist_ok=True)
os.chdir('spam')
example_file = 'file1.log'
with open(example_file, 'w', encoding='utf-8') as file_obj:
    file_obj.write('Hello' * 10000)
example_zip_file = 'file1.log.zip'


# + write mode will erase all existing contents of a ZIP file
# + append mode 'a'; if you want to simply add files to an existing ZIP file
with zipfile.ZipFile(example_zip_file, 'w') as example_zip:
    example_zip.write(example_file, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    # `compresslevel=9`: the slowest but most compressed level
    # the default is 6
    # 
# The `zipfile.ZipFile()` function opens a ZIP file in a `with` statement,
# in a manner similar to how the `open()` function opens files.
# This ensures that the `close()` method is automatically called
# when the execution leaves the `with` statement’s block.


# investigate the zip file

example_zip = zipfile.ZipFile(example_zip_file)
print(type(example_zip)) # <class 'zipfile.ZipFile'>
print(example_zip.namelist())
file1_info = example_zip.getinfo(example_zip.namelist()[0])
print(type(file1_info)) # <class 'zipfile.ZipInfo'>
print(file1_info.file_size, file1_info.compress_size)
print(f'Compressed file is {round(file1_info.file_size / file1_info.compress_size, 2)}x smaller!')
example_zip.close()


example_zip = zipfile.ZipFile(example_zip_file)
# example_zip.extractall() # to the current working directory
example_zip.extractall(h / 'spam2')
example_zip.close()


example_zip = zipfile.ZipFile(example_zip_file)
example_zip.extract(str(example_file), h / 'spam3')
example_zip.close()


# clear(test)

send2trash.send2trash([h / 'spam', h / 'spam2', h / 'spam3'])
os.chdir(h)
print(Path.cwd())


