def fileRead(fname):
    with open(fname,"r") as myfile:
        list1=myfile.readlines()
        print(list1)

fileRead("text1.txt")
