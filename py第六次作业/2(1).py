def mySum(a,n):
    a=str(a)
    s=0
    c=0
    for i in range (1,n+1):
        c=int(i*a)
        s+=c
    return(s)
x,y=eval(input())
print (mySum(x,y))
