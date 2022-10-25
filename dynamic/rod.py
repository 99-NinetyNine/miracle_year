"""
from CLRS book
"""
def rod(p,n):
    if n ==0:
        return 0
    q=-1
    for i in range(1,n+1):
        q=max(q,p[i]+rod(p,n-i))
    return q


def memoized_rod(p,n,r):
    if(r[n]>=0):
        return r[n]
    q=-1
    if(n==0):
        q=0
    else:
        for i in range(1,n+1):
            q=max(q,p[i]+memoized_rod(p, n-i, r))
    r[n]=q
    return q

def bottom_up_rod(p,n,r):
    r=[-1]*(n+1)
    r[0]=0
    
    for j in range(1,n+1):
        q=-1
        for i in range(1,j+1):
            q=max(q,p[i]+r[j-i])
        r[j]=q
    return r[n]

def enhanced(p,n):
    r=[-1]*(n+1)
    r[0]=0
    s=[-1]*(n+1)
    
    for j in range(1,n+1):
        q=-1
        for i in range(1,j+1):
            if(q<p[i]+r[j-i]):
                q=p[i]+r[j-i]
                s[j]=i
        r[j]=q
    return r,s

def print_soln(p,n):
    r,s=enhanced(p, n)
    while n>0:
        print(s[n],"\n")
        n=n-s[n]

def try_dynamic(p,n):
    r=[-1]*(n+1)
        
    res=rod(p, n)
    print("recursion:\t",res)

    res=memoized_rod(p,n,r)
    print("memoized:\t",res)

    res= bottom_up_rod(p,n,r)
    print("bottom:\t",res)
    
    print("soln:")
    print_soln(p, n)

try_dynamic([0,1,5,8,9,10,17,17,20,24,30],10)