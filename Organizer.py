import os
import shutil

path='/home/arun/Pictures'
listoffiles=os.listdir(path)


for files in listoffiles:
    name,extension=os.path.splitext(files)
    print(files)
    extension=extension[1:]

    if not os.path.exists(f'{path}/{extension}'):
        os.makedirs(f'{path}/{extension}')
    shutil.move(f'{path}/{files}', f'{path}/{extension}/{files}')
