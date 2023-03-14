x,n=list(map(int,input().split()))
l=0
while n>0:
    if x==6:
        x=x+1
        n=n-1
    elif x==7:
        x=x+1
        n=n-1
    else:
        x=x+1
        n=n-1
        l=l+250
print(l)