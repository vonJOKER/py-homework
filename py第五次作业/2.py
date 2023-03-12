a=str(input())
b = a[0]
# print(b,a)
if a.isalnum()==True and b.isalpha()==True:
    print("Yes")
elif '_' in b:
    print("Yes")
else:
    print("No")