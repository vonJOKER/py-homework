n=int(input())
a=[]
for i in range(1,n+1):
    if n/i==int(n/i):
        a.append(i)
print(a)