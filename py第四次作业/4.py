n=eval(input("please input a three-digit number:"))
if 100<=n<=999:
    c=int(n%10)
    b=int(((n-c)/10)%10)
    a=int((n-c-10*b)/100)
#print(a,b,c)
    if a*a*a+b*b*b+c*c*c==n:
        print("true")
    else:
        print("false")
else:
    print("error")
