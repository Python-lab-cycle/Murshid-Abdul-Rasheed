astr=input("enter the string\n")
char=input("enter the character\n")
print("given string : ",astr)
print("given character",char)
res=0
for i in range(len(astr)):
    if(astr[i]==char):
        res=res+1
print("number of times character is present in string : ",res)
