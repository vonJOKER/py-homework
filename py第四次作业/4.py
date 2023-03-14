isbn = input()
# isbn = str("978-7-121-28484-3")
# print(isbn)
b = {}
k = 1
for i in range(0, 17):
    if isbn[i].isnumeric():
        b[k] = isbn[i]
        k = k + 1
# print(b)
k = 1
a = 0
while k <= 12:
    if k % 2 == 1:
        a = int(b[k]) + a
    else:
        a = a + 3 * int(b[k])
    k += 1
var = 10 - (a % 10)
if var == 10:
    var = 0
if int(var) == int(b[13]):
    print("Right")
else:
    isbn=list(isbn)
    isbn[-1]=str(var)
    isbn=''.join(isbn)
    print(isbn)
# replace函数好像不能只替换字符串中某一个，而是把出现过的全部替换了
# 这里把他先转化成列表再对列表中特定元素进行替换然后再输出成特定格式