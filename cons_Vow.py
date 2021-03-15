wrd=input().split()
v=["a","e","i","o","u"]
for i in wrd:
    sav=[]
    for j in i:
        if(j in v):
            sav.append(i.index(j))
    if(len(sav)>1):
        sums=max(sav)-min(sav)
        if(sums==1):
            print(i)