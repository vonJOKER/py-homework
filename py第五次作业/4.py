n=int(input("Please input an integer which is between 2 and 99:"))
a=[]
for i in range(1,n):
    if i%2==1:
        a.append(i)
print(a)