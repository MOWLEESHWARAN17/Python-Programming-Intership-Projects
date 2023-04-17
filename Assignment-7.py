#Create the following dictionary and perform the following operations  D={1: 100, 2: 200, 3: 300} 
#i) Display the data at the key 2. 
#ii) Append the data 400 using the key 4. 
#iii) Delete the value at key 3.


# Create a dictionary
D = {1: 100, 2: 200, 3: 300}

# Display the data at key 2
print("Data at key 2:", D[2])

# Append the data 400 using the key 4
D[4] = 400
print("Updated dictionary:", D)

# Delete the value at key 3
del D[3]
print("Updated dictionary:", D)


