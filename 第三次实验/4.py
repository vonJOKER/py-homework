a=input("numbers:").split(',')
a=[eval(i) for i in a]
d=[]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==9:
            x,y=min ((a[i],a[j])),max ((a[i],a[j]))
            d.append((x,y))
d=list(set(d))
d.sort()
print(d,sep='')