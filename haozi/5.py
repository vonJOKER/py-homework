n=input("Sex(F or M):")
m=int(input("Age(1-120):"))
if n=="F":
    if 120>=m>=20:
        print("Yes")
    elif 0<m<20:
        print("No")
    else:
        print("Error")
elif n=="M":
    if 120>=m>=22:
        print("Yes")
    elif 0<m<22:
        print("No")
    else:
        print ("Error")
else:
    print("Error")