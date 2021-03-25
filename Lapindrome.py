'''laipindrome,, i/p :xyzzxy,,,, i/p: abckk'''
wrd=input()
c=0
l=int(len(wrd)/2)
if(l%2==0):
    a=wrd[0:l]
    b=wrd[l:len(wrd)]
else:
    a=wrd[0:l]
    b=wrd[l:len(wrd)]
for i in a:
    if(i in b):
        c+=1
if(c==len(a)):
    print("yes its a lapindrome")
else:
    print("No its not")