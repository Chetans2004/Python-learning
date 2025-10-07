# # # n Python, a list is a built-in data structure that can hold an ordered collection of items. Unlike arrays in some languages, Python lists are very flexible:

# # # Can contain duplicate items
# # # Mutable: items can be modified, replaced, or removed
# # # Ordered: maintains the order in which items are added
# # # Index-based: items are accessed using their position (starting from 0)
# # # Can store mixed data types (integers, strings, booleans, even other lists)

# # #Creating a List usnig square [] brckets
# # # numbers=[1,2,3,4,5]

# # #Accessing List Elements usnig index position
# # # print(numbers[2])

# # #Adding Elements into List 
# # # numbers.append(5) #This function will add the element at the end of the list
# # # print(numbers)

# # # numbers.extend([2,5,7]) #add multiple elements at the ed of list
# # # print(numbers)

# # # numbers.insert(2,100)#add the element at the give index
# # # print(numbers)

# # #1.Create a list of 5 numbers and print the first and last element
# # # numbers=[1,2,3,4,5]
# # # print(numbers[0])
# # # print(numbers[-1])


# # #2.Given a list [10, 20, 30, 40, 50], print the sum and average of the numbers.
# # # numbers=[10, 20, 30, 40, 50]
# # # print(sum(numbers))
# # # print(sum(numbers)/len(numbers))

# # #.Add "apple" to an empty list using append()
# # # fruits=[]
# # # fruits.append("Apple")
# # # print(fruits)


# # #Remove "banana" from the list ["apple", "banana", "cherry"].
# # # fruits=["apple", "banana", "cherry"]
# # # fruits.remove("banana")
# # # print(fruits)

# # #Find the length of the list [1, 2, 3, 4, 5, 6]
# # numbers=[1, 2, 3, 4, 5, 6]
# # print(len(numbers))

# #Given names = ["Chetan", "Shiva", "Ravi", "Anil"], print all names that start with 'A'.
# # names = ["Chetan", "Shiva", "Ravi", "Anil"]
# # for name in names:
# #         if name.startswith('A'):
# #             print(name)

# #Replace the second element in ["Python", "C++", "Java"] with "C".
# subjects=["Python", "C++", "Java"] 
# subjects[1]="c"
# print(subjects)

#Slice the list [1, 2, 3, 4, 5, 6, 7] to get only even-indexed elements.
# numbers=[1, 2, 3, 4, 5, 6, 7]

# print(numbers[1: :2])

