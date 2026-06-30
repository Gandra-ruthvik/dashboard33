






L=["warangal", "hyderabad", "vizag", "vijayawada", "tirupati"]
print(L[2])
print(L[0:3])
L.sort()
print(L)
L.append("narsampet")
print(L)    
L.remove("hyderabad")
print(L)
def len_list(input_list):
    return len(input_list)

print("The length of the list is:", len_list(L))
