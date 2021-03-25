wrd=input()
l=[]
l1=[]
pos=[]
for i in range(len(wrd)):
    if(wrd[i].isalpha()):
        l.append(wrd[i])
    else:
        l1.append(wrd[i])
        pos.append(i)
l.reverse()
num=0
num1=0
for i in range(len(wrd)):
    if(i in pos):
        print(l1[num],end="")
        num+=1
    else:
        print(l[num1],end="")
        num1+=1