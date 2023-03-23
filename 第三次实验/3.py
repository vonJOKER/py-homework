a=int(input())
b=list(map(int,input().split()))
dic={}
for i in b:
    if i in dic:
        dic[i]+=1
        print(dic[i],end=' ')
    else:
        dic[i]=1
        print(dic[i],end=' ')