#Armstrong Num.
x=int(input())
y=int(input())
for i in range(x,y):
    sav=0
    for j in str(i):
        sav+=int(j)**3
    if(sav==i):
        print(i,"is a Armstrong Number")
    else:
        print(i,"is not a Armstrong Number")

