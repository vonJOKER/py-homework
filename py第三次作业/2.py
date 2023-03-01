y=1
k=1
n=1
while y<3:
    k=k+2
    n=n+1
    y=y+(1/k)
y=round(y-(1/k),2)
print("n=" + str(n-1)+ ",y=" + str(y))