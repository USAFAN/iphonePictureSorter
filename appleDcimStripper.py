#place dcim from iphone somewhere on a drive other then the iphone/ copy the dcim folder to ur desktop or sumthing

import os

import shutil

basePath = 'C:\\user\\DCIM' # path to apple dcim folder needs to be copied off iphone first

placeToDump ='C:\\user\\exampleTargetFolder'

i = 0

def folderUnwrapper(basePath):
    print("FOLDER UNWRAPPER")
    global i
    with os.scandir(basePath) as entries:
        for entry in entries:
            if entry.is_file():
                i += 1
                print(entry.name)
                print(i)
                shutil.copy(entry.path,placeToDump)
                # add remove option later
            if entry.is_dir():
                folderUnwrapper(entry.path)
                with os.scandir(entry.path) as folderheld:
                    for fileheld in folderheld:
                        if fileheld.is_file():
                            continue


folderUnwrapper(basePath)
