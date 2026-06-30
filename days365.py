d=int(input("Enter no.of days:"))
if d>=365:
    days365=d//365
    d=d%365
    print("A Year",days365)
    print("days",d)
