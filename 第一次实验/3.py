(a,b,c,d)=eval(input("four scores:"))
z=a+b+c+d
if a<60 or b<60 or c<60 or d<60 or z<340:
    print("not")
else:
    if z<370:
        print("pay")
    else:
        print("free")
