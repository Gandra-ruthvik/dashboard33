d=int(input("Enter a value:"))
if d>=0 and d<=9:
    print("one digit")
elif d<=99:
    print("two digit")
elif d<=999:
    print("three digit")
else:
    print("only avaliable one digit and two digits and three digits")
