(y,m)=eval(input("year,month:"))
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("31")
elif m==4 or m==6 or m==9 or m==11:
    print("30")
else :
    if (y/4==int(y/4) and y/100!=int(y/100)) or y/400==int(y/400):
        print("29")
    else :
        print("28")

