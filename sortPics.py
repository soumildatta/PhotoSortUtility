import os
import shutil
from sys import exit

def copyFiles(folder, fileList):
    for filename in fileList:
        print(filename)
        old_path = f'./{folder}'
        new_path = f'./{folder}/jpeg' if str.lower(filename).endswith(".jpg") else f'./{folder}/raw'
        source = os.path.join(old_path, filename)
        destination = os.path.join(new_path, filename)
        dest = shutil.copyfile(source, destination)

if __name__ == "__main__":
    items = os.listdir('./')
    folders = []
    for item in items:
        if os.path.isdir(item) and item != 'Lightroom':
            folders.append(item)

    if len(folders) == 0: 
        print("There are no folders to sort")
        exit()

    for folder in folders:
        curr_dir = os.walk(f'./{folder}')
        if 'raw' in curr_dir and 'jpeg' in curr_dir:
            copyFiles(folder, curr_dir)
        else:
            try:
                os.mkdir(f'./{folder}/jpeg')
                os.mkdir(f'./{folder}/raw')
                copyFiles(folder, curr_dir)
            except:
                print(f'Process might have already been completed for the folder: {folder}')
                exit()
    
    print('Process completed.\nYou can now check and delete the files outside of the "raw" and "jpeg" folders.')
