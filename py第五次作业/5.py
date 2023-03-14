n=int(input())
a="z"
for i in range(1,n+1):
    country=input()
    b=str(country)
    if b<=a:
        a=b
        c=country
print(c)