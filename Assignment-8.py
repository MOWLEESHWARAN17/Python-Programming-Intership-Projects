#Create the following sets Set A={1,2,3,4,5} Set B={4,5,6,7,8} Perform the following operations on the above sets. 
#1. Intersection 
#2. Union 
#3. Difference 
#4. Symmetric difference


# Create the sets
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Intersection of sets A and B
intersection = A.intersection(B)
print("Intersection of A and B:", intersection)

# Union of sets A and B
union = A.union(B)
print("Union of A and B:", union)

# Difference between sets A and B
difference = A.difference(B)
print("Difference of A and B:", difference)

# Symmetric difference between sets A and B
symmetric_difference = A.symmetric_difference(B)
print("Symmetric difference of A and B:", symmetric_difference)

