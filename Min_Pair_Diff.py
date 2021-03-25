'''find min diff in list'''
n=input().split(",")
mini=0
l=[]
for i in n:
    sums=0
    for j in n:
        sums=int(j)-int(i)
        if(sums>0):
            l.append(abs(sums))
print(min(l))
