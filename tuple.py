cities = ("New York", "Los Angeles", "Chicago", "Houston", "Phoenix")
print(cities)
def firstlast(cities):
    return cities[0], cities[-1]
studentdetails=(("John", 20, "A"), ("Alice", 22, "B"), ("Bob", 19, "C"))
print(studentdetails)
def studentname(studentdetails):
    names = []
    for x in studentdetails:
        names.append(x[0]) 
    names.sort()
    return names
print(studentname(studentdetails))
def unpackelements(tuple_input):
    v1, v2, v3 = tuple_input
    print("Unpacked values:")
    print("Value 1:", v1)
    print("Value 2:", v2)
    print("Value 3:", v3)
my_tuple = (10, 20, 30)
unpackelements(my_tuple)