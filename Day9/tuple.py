# # #Tuples
# # #-are immutable means can't change,delete,add elements in tuple
# # #Indexing
# # #slicing
# # #Aloow Duplicate values
# # #Allow Nested tuples
# # #concatenation is possible
# # #we can convert list into tuples

# # tup=(10,20,30)
# # # print(tup[1])

# # # print(tup[0:2])
# # # tup1=(10,20,(20,40),10)
# # # # print(tup1)

# # # print(tup+tup1)

# # # list1=[10,20,30]
# # tup2=(tuple(list1))
# # print(type(tup2))


# #Prwctice questions
# #Create a tuple of 5 numbers. Print the first and last element.
# # tupl=(10,20,30,40,50)
# # print(tupl[0])
# # print(tupl[-1])



# Create a tuple of 3 strings (e.g., "apple", "banana", "cherry") and print it in reverse order.
# strings=( "apple", "banana", "cherry")
# rev=strings[::-1]
# print(rev)

# Create a tuple (1, 2, 3, 2, 1) and count how many times 2 occurs.
# tup=(1,2,3,2,4,2)
# count=tup.count(2)
# print(count)

#Create a tuple (10, 20, 30, 40, 50) and slice it to get (20, 30, 40).
# tup=(10,20,30,40,50)
# print(tup[1:4])

# Create a tuple with numbers. Ask the user to input a number and check if it exists in the tuple.
# tup=(10,20,30,40,50)
# tup_number=int(input("Enter your numver"))
# if tup_number in tup:
#     print(f"{tup_number} present in {tup}")
# else:
#      print(f"{tup_number} not present in {tup_number}")

# 

# Convert a tuple (1, 2, 3, 4) into a list, append a new number, and convert it back to a tuple
# tup=(1, 2, 3, 4)
# list1=[tup]
# list1.append(20)
# tup2=tuple(list1)
# print(type(tup2))