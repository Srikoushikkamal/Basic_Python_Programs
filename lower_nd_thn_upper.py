wrd=input()
up=[]
down=[]
for i in wrd:
    if(i.isupper()):
        up.append(i)
    else:
        down.append(i)
print(*down+up)