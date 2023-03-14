n = int(input())
m = int(input())
zlc = n  # 总路程
for i in range(1, m + 1):
    n = n / 4
    zlc = zlc + 2 * n
print('%.2f' % (zlc - 2 * n))
print('%.2f' % n)
