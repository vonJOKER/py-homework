import math as m
time=eval(input("time:"))
if time<0.5 :
    m=0
else:
    time=m.ceil(time)
    m=5*time
if m>50:
    m=50
print(m)
