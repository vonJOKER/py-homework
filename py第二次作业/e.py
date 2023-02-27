sex=input("Sex(F or M):")
Age=int(input("Age(1-120):"))
'''if sex!="F" and sex!="M":
    print("Error")
if Age>120 or Age<1:
    print("Error")
'''

if (sex=="M" and 120>=Age>=22) or (sex=="F" and 120>=Age>=20):
    print("Yes")
elif (sex=="M" and 1<=Age<22) or (sex=="F" and 1<=Age<20):
    print("No")
else :
    print("Error")