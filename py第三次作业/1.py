import random as r
r.seed(10)
mima = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
mm = ""
long = int(input())
for i in range(long):
    mm+=mima[r.randint(0,len(mima)-1)]
print(mm)