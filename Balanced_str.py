s1=input()
s2=input()
c=0
for i in s1:
    if(i in s2):
        c+=1
if(c==len(s1)):
    print("Yes string is balanced")