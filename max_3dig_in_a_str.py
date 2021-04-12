s,maxx=input(),0
for i in range(len(s)-2):
    if(int(s[i:i+3])>maxx):
        maxx=int(s[i:i+3])
print(maxx)