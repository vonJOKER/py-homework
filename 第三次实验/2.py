n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
a.sort()
m=a[int(n/2)]
f=a.index(m)
a.reverse()
b=a.index(m)
if f==b:
    print(m)
else:
    print(-1)