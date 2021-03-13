import math
def find(s1,s2):
    l1=math.ceil(len(s1)/2)-1
    l2=math.ceil(len(s2)/2)-1
    sol=s1[0],s2[0],s1[l1],s2[l2],s1[-1],s2[-1]
    print(*sol)
if __name__=="__main__":
    s1=input()
    s2=input()
    find(s1,s2)