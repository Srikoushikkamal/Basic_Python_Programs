#Capitalize first letter in a str

wrd=input().split(" ")
for i in wrd:
    for j in range(len(i)):
        if(j==0):
            print(i[j].upper(),end="")
        else:
            print(i[j],end="")
    print()
            