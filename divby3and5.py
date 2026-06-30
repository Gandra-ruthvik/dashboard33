d=int(input("Enter a Value:"))
if d%3==0 and d%5==0:
    print("it is divisible both numbers")
elif d%3==0:
    print("divisible by 3 but not 5")
elif d%5==0:
    print("divisible by 5 but not 3")
else:
    print("it is not divisible by 3 and 5")