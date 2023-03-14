a = list(input().split(' '))
del a[0]
a.reverse()
for i in range(1, len(a) + 1):
    print(a[i-1], end=" ")
