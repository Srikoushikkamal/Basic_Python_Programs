wrd=input().split()
l=[]
for i in wrd:
    for j in range(len(i)-1,-1,-1):
        print(i[j],end="")
    print(end=" ")