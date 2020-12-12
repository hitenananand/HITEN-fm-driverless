#consider a tuple
tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)

# printing original tuple
print("The original tuple is : " + str(tup))

# Removing duplicates from tuple
res = tuple(set(tup))

# printing result
print("The tuple after removing duplicates : " + str(res))
total=0
for ele in range(0, len(res)):
    total = total + res[ele]

# printing total value
print("Sum of all elements in given list: ", total)
