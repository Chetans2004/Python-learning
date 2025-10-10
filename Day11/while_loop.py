# In Python, a while loop is used to execute a block of statements repeatedly until a
#  given condition is satisfied. 
# When the condition becomes false, the line immediately after the loop in the program is executed.
# cnt = 0
# while (cnt < 3):
#     cnt = cnt + 1
#     print("Hello")
# total=0
# numbers=int(input("Enter number (If you want to quit enter 0)"))
# while numbers!=0:
#     total+=numbers
#     numbers=int(input("Enter number (If you want to quit enter 0 or -1)"))
# print(total)

# Multiplication Table
# Take a number as input and print 
# its multiplication table up to 10 using a while loop.
# multiplaction_table=int(input("Enter which multiplication atble you want"))
# multi=1
# while multi<=10:
#     table=multiplaction_table*multi
#     print(f"{multiplaction_table} * {multi} = {table}")
#     multi+=1

# Ask the user for a number and print a countdown till 1.
# count_down=int(input("Enter anumber"))
# count=count_down
# while count>=0:
#     print(count)
#     count-=1
# print("Blast off! 🚀")


# Sum Until 0 Entered

# Keep asking the user for numbers.
# Stop when they enter 0 and print the total sum.
# number=int(input("Enter numbers (Enter Quit for 0)"))
# total=0
# while number !=0:
#    total+=number
#    number=int(input("Enter numbers (Enter Quit for 0)"))
# print(total)

# Ask the user to enter a password.
# Keep asking until the correct password ("python123") is entered.
# password=(input("Enter a passowrd"))
# correct_password="python123"
# while password != correct_password:
#     password=(input("Enter a passowrd"))
# print(password)

# Factorial of a Number
# Find the factorial of a given number using a while loop.
number=int(input("Enter number"))
fact=1
while number >0:
    fact=fact*number
    number-=1
print(fact)

