ch=input("please input a char:")
if ch.isalnum()==True:
    if ch.isalpha()==True:
        print("alphabet character")
    else:
        print("digital character")
else:
    print("others character")
