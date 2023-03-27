def sumyinzi(n):
    ls = [1,]
    for i in range(2,n):
        if n%i==0:
            ls.append(i)
    return sum(ls)

def sumElem(n):
    mydict = {}
    for i in range(2,n+1):
        mydict[i] = sumyinzi(i)
    result = []
    for i in mydict:
        if mydict[i] in mydict and i==mydict[mydict[i]] and i!=mydict[i]:
            result.append((min(i,mydict[i]),max(i,mydict[i])))
    result = list(set(result))
    result.sort()
    [print(i,j) for i,j in result]
a = eval(input())
sumElem(a)
