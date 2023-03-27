def oddNumSum(x,y):
    n=0
    c=0
    for i in range(1,x+1,2):
        n+=i
        c+=1
        if n>=y:
            return n,c,i
    else:
            return n,c,i
p=int(input())
q=int(input())
i,j,k=oddNumSum(p,q)
print (i)
print (j)
print (k)
