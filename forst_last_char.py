s1=input()
find=input()
cnt=[]
for i in range(len(s1)):
    if(find==s1[i]):
        cnt.append(i)
if(len(cnt)>1):
    print(cnt[0],cnt[-1])
else:
    print("Invalid Input")