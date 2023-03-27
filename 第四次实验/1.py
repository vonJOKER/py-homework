def countn(str1):
    a=0
    for i in str1:
        if i.isalpha():
            a+=1
    return a
str1=input()

print(countn(str1))