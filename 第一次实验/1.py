distance=int(input("Please input a number of distance:"))
Walk=distance/2
Bike=distance/4+50
if Walk>Bike:
    print("Bike")
elif Walk<Bike:
    print("Walk")
else:
    print("All")
