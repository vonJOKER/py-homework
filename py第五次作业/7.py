n = input()
if n[3] == '-' and n[8] == '-' and len(n) == 13:
    a = list(n)
    del a[3]
    del a[7]
    for key in a:
        if key.isdigit() == True:
            a = "True"
        else:
            a = "False"
            break
    print(a)
else:
    print("False")
