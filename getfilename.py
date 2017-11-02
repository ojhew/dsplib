def getfilename():
    path = input("Enter file path: ")
    params = path.split("/")
    filename = (params[len(params)-1])
    print(filename)
    return filename