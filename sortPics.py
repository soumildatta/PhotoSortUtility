import os
import shutil
from sys import exit

def copyFiles(folder, fileList):
    for filename in fileList:
        old_path = folder
        new_path = f'{folder}/jpeg' if str.lower(filename).endswith(".jpg") else f'{folder}/raw'
        source = os.path.join(old_path, filename)
        destination = os.path.join(new_path, filename)
        dest = shutil.copyfile(source, destination)

if __name__ == "__main__":
    folders = []
    originalPath = os.path.abspath('./')
    items = os.listdir('./')

    for item in items:
        if os.path.isdir(os.path.abspath(item)) and item != 'Lightroom':
            folders.append(os.path.abspath(item))

    if len(folders) == 0: 
        print("There are no folders to sort")
        exit()

    for folder in folders:
        curr_dir = os.walk(folder)
        for root, dirs, files in curr_dir:
            if 'raw' in dirs and 'jpeg' in dirs:
                copyFiles(folder, files)
            else:
                try:
                    os.mkdir(f'{folder}/jpeg')
                    os.mkdir(f'{folder}/raw')
                    copyFiles(folder, files)
                except:
                    print(f'Process might have already been completed for the folder: {folder}')
                    exit()

    print('Script finished running')
