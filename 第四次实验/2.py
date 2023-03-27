def isRepeated(v):
    x=set(v)
    if len(x)==len(v):
        return False
    return True
n=input().split(",")
print(isRepeated(n))