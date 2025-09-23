# Copies an entire folder and its contents into a ZIP file whose filename increments

import zipfile, os
from pathlib import Path
import send2trash


def backup_to_zip(folder):
    # Back up the entire contents of "folder" into a ZIP file.
    folder = Path(folder)  # Make sure folder is a Path object, not string.

    # Figure out the ZIP filename this code should use, based on what files already exist.
    number = 1
    while True:
        zip_filename = Path(folder.parts[-1] + '_' + str(number).zfill(3) + '.zip')
        if not zip_filename.exists():
            break
        number = number + 1

    # Create the ZIP file.
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')
    print(backup_zip)

    # Walk the entire folder tree and compress the files in each folder.
    for folder_name, subfolders, filenames in os.walk(folder):
        folder_name = Path(folder_name)
        print(f'Adding files in folder {folder_name}...')

        print('(참고) subfolders:', subfolders)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            print(f'Adding file {filename}...')
            backup_zip.write(folder_name / filename)

    backup_zip.close()
    print(f'Done({os.path.getsize(zip_filename)})')


# ready(test)

# h = Path.home()
h = Path.cwd()
(h / 'spam').mkdir(exist_ok=True)
(h / 'spam' / 'spam2').mkdir(exist_ok=True)
with open(h / 'spam/spam2/file1.log', 'w', encoding='utf-8') as file:
    file.write('Hello\n')


# run(test)

backup_to_zip(h / 'spam' / 'spam2')


# clear(test)

send2trash.send2trash([h / 'spam', 'spam2_001.zip'])
# send2trash.send2trash(['spam2_002.zip', 'spam2_003.zip'])


