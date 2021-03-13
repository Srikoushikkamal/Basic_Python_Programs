s1=input()
vow=0
num=0
con=0
v=["a","e","i","o","u"]
for i in s1:
    if(i.isnumeric()):
        num+=1
    elif(i in v):
        vow+=1
    else:
        con+=1
print("Digits:",num)
print("vowels:",vow)
print("Consonants:",con)