(a,b,c)=eval(input("please input three numbers:"))
if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
    if (a*a+b*b)==c*c or (a*a+c*c)==b*b or (b*b+c*c)==a*a:
        print("right triangle")
    elif a==b and a==c:
        print("equilateral triangle")
    else:
        print("ordinary triangle")
else:
    print("false")
