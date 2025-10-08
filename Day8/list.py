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
# # # list1=[10,34,90,['Mohan','Shayam','Ram'],89]
# # # a=list1[3][2]
# # # print(a)

# # # list1=[1,1,1]
# # # list2=[1,1,1]
# # # list3=[1,1,1]
# # # matrix=[list1,list2,list3]
# # # print(f"{list1}\n{list2}\n{list3}\n")
# # # position=input("Enter position where you want to hide your money")
# # # row_number=int(position[0])
# # # column_number=int(position[1])
# # # selected_row=matrix[row_number-1]
# # # selected_row[column_number-1]='X'

# # # print(f"{list1}\n{list2}\n{list3}\n")

# # Create a 3×3 matrix filled with 0s.
# # Ask the user to enter a position (like "12") and change that position to 9.
# # Then print the updated matrix
# list1=[0,0,0]
# list2=[0,0,0]
# # list3=[0,0,0]
# # print(f" {list1}\n {list2}\n {list3}\n")
# # position=input("enter a position")
# # matrix=[list1,list2,list3]
# # row_number=int(position[0])
# # column_number=int(position[1])
# # selected_row=matrix[row_number-1]
# # selected_row[column_number-1]=9
# # print(f" {list1}\n {list2}\n {list3}\n")


# # Make a 4×4 matrix filled with *.
# # Ask the user to enter a position (like "34") and replace that position with "@"

# list1=[2,2,2]
# list2=[2,2,2]
# list3=[2,2,2]
# list4=[2,2,2]
# print(f"{list1} \n {list2} \n{list3} \n{list4} \n")
# nested_list=[list1,list2,list3,list4]
# position=input("Enter your Position")
# row_number=int(position[0])
# column_number=int(position[1])

# selected_row=nested_list[row_number-1]
# selected_row[column_number-1]=9
# print(f" {list1}\n {list2}\n {list3}\n{list4}")



 