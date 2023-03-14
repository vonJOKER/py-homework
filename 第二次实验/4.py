s = input("Please input a integer:")[::-1]
o = 0
e = 0
for i in range(1, len(s) + 1):
    if i % 2 == 1:
        o = o + int(s[i - 1])
    else:
        e = e + int(s[i - 1])
print(o)
print(e)
if (e - o) % 11 == 0:
    print("TRUE")
else:
    print("FALSE")
