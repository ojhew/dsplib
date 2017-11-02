import hashlib

def getmd5hash(fc):
    m = hashlib.md5()
    m.update(fc)
    print(m.hexdigest())
    return m.hexdigest()

def getmd5hash():
    path = input("Enter file path: ")
    try:
        fo = open(path, "rb");
        fstr = fo.read();
        hashStr = getmd5hash(fstr)
        print(hashStr);
        fo.close();
    except:
        print("File not found")
