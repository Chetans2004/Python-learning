# # numbers=input("Enter the numbers seperated with space")
# # numbers_list=numbers.split()
# # cont=0
# # for i in numbers_list:
# #     cont+=1
# # print(cont)
# # maximum_number=numbers_list[0]
# # for i in numbers_list:
# #     if  i>maximum_number:
# #         maximum_number=i
# # print("Maximun number is",maximum_number)

# # A for loop is used to iterate over a sequence 
# # (such as a list, tuple, string, or range) or other iterable objects.
# # It executes a block of code once for each item in the sequence. 

# var=[10,30,28,10]
# for i in var:
#     print(i)

# va

# for i in (10,20,30):
#     print(i)
# sum1=0
# for i in range(2,101):
#     if i%2==0:
#          print(i) 


# # Ask user how many numbers to print
# count = int(input("Enter how many numbers you want to print: "))

# # Use for loop to print that many numbers
# for i in range(1, count+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
# #     else:
#         print(i)
# import random
# print("Welcome to Password Generator")
# letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
#         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
#         'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
#         'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
#         'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers=['0','1','2','3','4','5','6','7','8','9']
# symbols=['!','@','#','$','%','^','&','*','(',')','_','+']
# n_letters=int(input("How many letters would you like in your password"))
# n_symbols=int(input("How many Symbols would you like in your password"))
# n_numbers=int(input("How many Numbers would you like in your password"))
# password_list=[]
# for i in range(1,n_letters+1):
#     char=random.choice(letters)
#     password_list+=char
# # print(password)
# for i in range(1,n_symbols+1):
#     simb=random.choice(symbols)
#     password_list+=simb
# # print(password)
# for i in range(1,n_numbers+1):
#     num=random.choice(numbers)
#     password_list+=num

# random.shuffle(password_list)
# passowrd=""
# for char in password_list:
#     passowrd+=char
# print(passowrd)


# Dice Rolling Simulator 🎲 Simulate rolling a dice. 
# Let the user choose how many dice to roll. 
# Output the random results and total sum.
import random
print("Welcome to Dice Rolling Simulator 🎲")
rolls=int(input("How many dice would you like to roll? "))
rolls_result=[]
for i in range(1,rolls+1):
    dice=random.randint(1,6)
    rolls_result.append(dice)
total=sum(rolls_result)
print("Dice rolls:", rolls_result)
print("Total sum:", total)



