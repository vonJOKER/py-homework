s=input()
n=''
for i in s:
    if 'A' <=i<='Z':
        p=ord(i)-65
        new=chr(26-p-1+65)
        n=n+new
    elif 'a'<=i<='z':
        p=ord(i)-97
        new=chr(26-p-1+97)
        n=n+new
    else:
        n=n+i
print(s)
print(n)