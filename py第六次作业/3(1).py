def isLeap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
def days(year, month):
    lst = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeap(year):
        lst[1] = 29
    return lst[month-1]
x,y,z = map(int, input ().split('/'))
s = sum(days(x, i) for i in range(1, y))
print (s+z)
