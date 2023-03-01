(a,b)=eval(input("year,month:"))
if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
    print("31")
elif b==4 or b==6 or b==9 or b==11:
    print("30")
else :
    if (a/4==int(a/4) and a/100!=int(a/100)) or a/400==int(a/400):
        print("29")
    else :
        print("28")
