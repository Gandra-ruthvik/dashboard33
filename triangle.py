t1=int(input("Enter First Angle:"))
t2=int(input("Enter Second Angle:"))
t3=int(input("Enter Third Angle:"))
if t1>0 and t2>0 and t3>0:
    if t1+t2+t3==180:
        print("it is a valid triangle")
    else:
        print("invalid triangle`")
else:
    print("enter correct angles")
   