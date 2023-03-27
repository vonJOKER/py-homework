def sumThree(n):
    sum=0
    for i in range(1,int(n)+1):
        if i%2!=0:
            sum+=str(i).count("3")
    return sum
x=input("number:")
print(sumThree(x))
