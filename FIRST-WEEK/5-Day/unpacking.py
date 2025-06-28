coordinates = (1,2,3)
#multiply it each element of the index

#method one
result = coordinates[0]*coordinates[1]*coordinates[2]
print(result)

#method two
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

total = x*y*z
print(total)

#method three this method known as unpacking works on both on tuples and list

x,y,z = coordinates

totalunpackingresult = x*y*z
print(totalunpackingresult)