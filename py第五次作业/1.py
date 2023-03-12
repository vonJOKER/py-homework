an = input().split(' ')
# print(an)
a = int(an[0])
n = int(an[1])
# print(a,n)
i = 1
n1 = 0
while i <= n:
    n1 = (10 ** (n - i)) * a + n1
    i = i + 1

k = 2
n2 = 0
m = 1
while m <= n:
    if k <= n:
        n2 = n2 + (10 ** (n - k)) * a
        k = k + 1
        # print(n2)
    else:
        n1 = n1 - n2
        n = n - 1
        k = 2
        n2 = 0
        continue
print(n1)
