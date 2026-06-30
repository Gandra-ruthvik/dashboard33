u=input("Enter a value:")
if u in "ABCDEFGHIJKLMNOPURSTUVWXYZ":
    print("uppercase")
elif u in "abcdefghijklmnopurstuvwxyz":
    print("lowercase")
elif u in "0123456789":
    print("digits")
elif u in "!@#$%^&*":
    print("special character")
    