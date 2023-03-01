mima=str(input())
#print(str.isdigit())
if mima.isdigit()==True:
    for i in range(2,6):
        if mima[i]!=str((int(mima[i-1])+1)**3)[-1]:
            a="wrong"
            break
        else:
            a="right"
    print(a)
else:
    print("wrong")