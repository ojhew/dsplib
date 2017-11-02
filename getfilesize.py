import os

def getfilesize():
    filesize = 0
    path = input("Enter file path: ")
    try:
        statinfo = os.stat(path)
        size = statinfo.st_size
    except:
        print("File not found")
    return filesize