s1=input().split()
for i in s1:
    al=0
    num=0
    for j in i:
        if(j.isalpha()):
            al+=1
        elif(j.isnumeric()):
            num+=1
    if(al>0 and num>0):
        print(i)