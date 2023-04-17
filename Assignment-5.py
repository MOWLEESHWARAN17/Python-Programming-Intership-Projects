#Create a list m1=[1,2,3,4,5] and perform the following 
#i. Insert 100 at position 3 
#ii. Delete the number 4 
#iii. Append 200 
#iv. Print the list using for loop 
#v. Delete the list


# Create a list
m1 = [1, 2, 3, 4, 5]

# Insert 100 at position 3
m1.insert(2, 100)

# Delete the number 4
m1.remove(4)

# Append 200
m1.append(200)

# Print the list using for loop
for num in m1:
    print(num)

# Delete the list
del m1
