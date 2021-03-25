n=input()
sums=0
for i in n:
    fact=1
    for j in range(int(i),0,-1):
        fact*=int(j)
    sums+=fact
if(sums==int(n)):
    print("Its a krishnamoorthy number")
else:
    print("Its not a k.moorthy number")