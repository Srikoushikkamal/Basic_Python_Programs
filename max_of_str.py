wrd=input().split()
feq=0
sav=0
fin=0
l=[]
for i in wrd:
    for j in i:
        c=i.count(j)
        if(c>feq):
            feq=c
    if(feq>fin):
        fin=feq
        sav=i
print(sav)
