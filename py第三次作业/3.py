mlong=eval(input())
long=2
l=0
a=0
while l<mlong:
    l=l+long
    long=0.98*long
    a=a+1
print(a)