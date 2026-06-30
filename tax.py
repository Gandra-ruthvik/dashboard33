t=int(input("enter salary:"))
if t>0:
    if t<=250000:
        print("No tax")
    elif t<=500000:
        t=t-250000
        t=(t*5)/100
        print("5% tax",t)
    elif t<1000000:
        t=t-250000
        t=(t*7)/100
        print("7% ",t)
    elif t>=1000000:
        t=t-250000
        t=(t*10)/100
        print("10%",t)
else:
    print("enter a valid emount")