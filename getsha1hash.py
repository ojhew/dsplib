import hashlib

def getsha1hash(fc):
    m = hashlib.sha1()
    m.update(fc)
    print(m.hexdigest())
    return m.hexdigest()

def getsha1hash():
    path = input("Enter file path: ")
    try:
        fo = open(path, "rb");
        fstr = fo.read();
        hashStr = getsha1hash(fstr)
        print(hashStr);
        fo.close();
    except:
        print("File not found")
