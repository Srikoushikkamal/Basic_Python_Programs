#Factorial

#n=5
n=int(input())
fact=1
for i in range(n,0,-1):
    fact*=i
print(fact)
