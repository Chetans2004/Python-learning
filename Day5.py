#string slicing is a technique is used to access the substring of a string
# string="Chetan"
# string[0:4]
#


#String slicing third parameter ---It is also caled as step value
 #step value specifies the number of element to be skip when slicing the string
 #If the number is Positive slicing start form Forword order 
 #If the number is Negative slicing start form Backword order 
# string="Chetan"
# string[0:4:-1]

# s="I am Jaspeert"
# s[::-1]

#1.Given s = "PythonProgramming", print the first 6 characters
# s = "PythonProgramming"
# s1=s[0:6]
# print(s1)


#2.Print the last 5 characters of the string "ChetanShinagari"
# string ="ChetanShinagari"
# s1=string[:]
# print(s1)

#3Extract "thon" from "Python"
# s="Python"
# s1=s[2:]
# print(s1)



#4Given a string "India", print it in reverse order using slicing
# string="India"
# s1=string[::-1]
# print(s1)


#5Print every second character from "ABCDEFGHIJ"
# string="ABCDEFGHIJ"
# s1=string[0::2]
# print(s1)


#6.Given s = "HelloWorld", print characters from index 2 to index 7
# s = "HelloWorld"
# s1=s[2:8]
# print(s1)


#Extract "Shina" from "ChetanShinagari"
# s="ChetanShinagari"
# s1=s[6:11]
# print(s1)

#8Reverse only the first 5 characters of "Programming"
# s="Programming"
# s1=s[4::-1]
# print(s1)

#9From "abcdefg", print characters at odd positions
# s="abcdefg"
# s1=s[1::2]
# print(s1)




#10.Given a string "PythonIsFun", print it in reverse but skip every alternate character
# string ="PythonIsFun"
# s1=string[::2]
# print(s1)


#11.From "abcdefghijklmnop", print every 3rd character starting from index 2.
# s="abcdefghijklmnop"
# s1=s[2::3]
# print(s1)

#12.Write a program that asks the user for a string and prints
#  the first half and second half separately
# s=input("Enter sting")
# s1=len(s)//2
# first_half=s[:s1]
# second_half=s[s1]
# print(first_half)
# print(second_half)

#13.Given s = "PythonProgramming", reverse only the word "Programming" using slicing.
# s = "PythonProgramming"
# s1=s[-1:-12:-1]
# print(s1)


#14.Ask the user for a string and print it in reverse but skip every 2nd character.
# string=input("Enter string")
# s1=string[-1::-2]
# print(s1)

#15.Given s = "DataScience", extract "Science" without directly using index numbers
s = "DataScience"
s1=s[4:]
print(s1)