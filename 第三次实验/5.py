s=input()
dic={}
di={}
for i in s:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
m=max (dic.values())
for key in dic:
    if dic[key]==m:
        di[key]=dic[key]
for i,j in di.items():
    print("%s %d"%(i,j))