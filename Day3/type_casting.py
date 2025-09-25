#Type Casting is the method to convert the Python variable datatype 
# into a certain data type in order to perform the required operation by users.
# first_number=int(input("Enter first number"))
# second_number=int(input("Enter second number"))
# sum=(first_number+second_number)
# print(sum) 
'''In the above Example input() always returns data as a string.First we converted it string to 
    integer then we added both numbers
'''

# two_digit_number=input("Enter two digit number")
# # first_num=two_digit_number[0]
# # second_num=two_digit_number[1] 

# # print(int(first_num) + int(second_num))
# print(int(two_digit_number[0]) + int(two_digit_number[1]))

#Take the string "123.45" and convert it into a float.
# str1="123.45"
# print(float(str1))


#Convert the integer 55 into a string and concatenate it with " apples".
# integer=int(int(input("Enter number")))
# print(str(integer) + "Apples")

#Convert the float 10.75 into an integer.
# float_value=12.5
# print(int(float_value))



#Write a program that takes a user’s age as input (input() always gives string), 
# then convert it into an integer and print
# age=input("Enter your age")
# sum=int(age) + 5
# print("In 5 years, you will be" + str(sum) +"years old ")

#Convert the string "True" into a boolean value.
string="True"
print(bool(string))
print(type(string))