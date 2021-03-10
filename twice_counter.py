wrd=input().split()
l=[]
for i in wrd:
    cnt=wrd.count(i)
    if(cnt==2 and i not in l):
        l.append(i)
print(*l)
        