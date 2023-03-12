s=input().split(' ')
b=eval(s[0]*eval(s[1]))
for i in range(1,eval(s[1])):
    b-=eval(i*s[0])
print(b)