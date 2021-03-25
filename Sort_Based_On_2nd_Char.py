n=input().split()
l=[]
new=[]
for i in n:
    new.append(n[0])
    l.append(i[1:])
l.sort()
for i in range(len(l)):
    for j in range(len(n)):
        new1=n[j]
        if(new1[1:]==l[i]):
            print(new1[0]+l[i],end="")
    print(end=" ")