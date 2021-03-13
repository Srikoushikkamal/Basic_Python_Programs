s1=input()
s2=[]
for i in s1:
    if(i.isalpha()):
        s2.append(i)
        print(i,end="")
    elif(i.isnumeric()):
        s2.append(i)
        print(i,end="")
    elif(i==" "):
        print(" ",end="")
    else:
        s2.append("#")
        print("#",end="")
