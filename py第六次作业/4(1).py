def change(n):
    if n == 0:
        return '0'
    m = ''
    while n > 0:
        m = str(n % 2) + m
        n //= 2
    return m
n = int(input())
print(change(n))
