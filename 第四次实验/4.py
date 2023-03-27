def sushu(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
a = eval(input())
result = 'JH'
for i in range(2,a):
    if sushu(i) and a%i==0:
        if sushu(a//i):
            result += (str(a//i)+str(i))
            print(result)
            break
else:
    print('error')
