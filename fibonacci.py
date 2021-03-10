#Fib with limits

x=int(input())
y=int(input())
diff=y-x
a=1
b=-1
for i in range(diff):
    c=a+b
    if(c>x and c<y):
        print(c,end=" ")
    b=a
    a=c
