n = int(input())
dic = {}
for i in range(1, n + 1):
    a = input().split(' ')
    dic_name = str(a[0])
    dic[dic_name] = str(a[1])
y = str(input())
s=dic.get(y,'not found')
print(s)