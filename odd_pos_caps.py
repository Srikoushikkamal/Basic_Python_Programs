wrd=input()
for i in range(len(wrd)):
    if(i%2!=0):
        print(wrd[i].upper(),end="")
    else:
        print(wrd[i],end="")