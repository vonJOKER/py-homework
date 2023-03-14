n = int(input("number:"))
b = {}
k = 1
for i in range(2, n):
    # print(i)
    if n / i == int(n / i):
        b[k] = i
        k = k + 1
    else:
        continue
if b == {}:
    print(str(n) + " is prime")
else:
    print(list(b.values()))
