sfz = str(input().split())
a = sfz[8:16]
# print(a)
if int(sfz[18]) % 2 == 1:
    x = "M"
else:
    x = "F"
print(a[0:4] + "-" + a[4:6] + "-" + a[6:9])
print(x)
