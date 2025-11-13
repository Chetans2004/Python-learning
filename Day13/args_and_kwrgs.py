# *args → Arbitrary Positional Arguments
# Used when you don’t know how many positional arguments will be passed to your function.
# It collects all extra positional arguments into a tuple.

# def greet(*args):
#     print(args)

# greet("Chetan", "Shiva", "Ravi","Vishwa")

# def greet(*args):
#     for name in args:
#         print("Hello" ,name)
# greet("Chetan","Vishwa")    


# **kwargs → Arbitrary Keyword Arguments
# Used when you don’t know how many keyword arguments (key=value pairs) will be passed.
# It collects all extra keyword arguments into a dictionary.
# def details(**kwrgs):
#     for name,value in kwrgs.items():
#         print(name,value)
#     # print(kwrgs)
# details(name="Chetan",roll_num=21,age=23)


# Sum of Numbers:
# Write a function add_numbers(*args) that takes any number of numbers and returns their sum.
# def add_numbers(*args):
#     c=0
#     for i in args:
#         c+=i
#     print(c)
# add_numbers(9,8,0)

# Multiply Numbers:
# Write a function multiply(*args) that multiplies all numbers passed to it.
# def multiply(*args):
#     multi=1
#     for i in args:
#        multi=multi*i
#     print(multi)
# multiply(2,3)


# def find_max(*args):
   
#     print(max(args))
# find_max(10,30,100)

# Check for Key:
# Write a function check_key(**kwargs) that checks if the key 'age' exists in kwargs.
# def check_key(**kwrgs):
# #         if 'age' in kwrgs:
# #             print("it is present")
# # check_key(name="Chetan",age=21)

# def pos(n):
#     ## Write the code
#     i=n
#     while i<n:
#         print(i)
#         i+=1
# pos(4)

# def neg(n):
#     ##Write the code
#     i=n-1
#     while i>n:
#         print(i)
#         i-=1
# neg(-4)
# n=4
# if n < 0:
#     neg(n)
# elif n > 0:
#     pos(n)
# else:
#     print("already Zero")



# def neg(n):
#     i = n
#     while i <= 0:
#         print(i, end=' ')
#         i += 1
#     print()

# def pos(n):
#     i = n - 1
#     while i >= 0:
#         print(i, end=' ')
#         i -= 1
#     print()

# n = 0

# if n < 0:
#     neg(n)
# elif n > 0:
#     pos(n)
# else:
#     print("already Zero")

