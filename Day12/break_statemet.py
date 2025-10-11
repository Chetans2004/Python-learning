# he break statement in Python is used to exit
# or “break” out of a loop (either a for or while loop) prematurely, 
# before the loop has iterated through all its items or reached its condition
# for i in range(0,10):
#     if i==5:
#         break
#     print("hi")
#     print(i)

# Keep asking the user to enter a number — stop the loop if they enter 0.
# numbers=int(input("Enter number"))
# while True:
#     numbers=int(input("Enter number"))
#     if numbers==0:
#         break
#     print(numbers)

# Print all numbers from 1 to 20, but stop when a number is divisible by 7.
# for i in range(1,21):
#     if i%7==0:
#         break
#     print(i)

# Find the first number between 1 and 50 that is divisible by both 3 and 5.
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print(i)
#         break


# Write a program that keeps asking for a password.
# If the password is “chetan”, break the loop.
# # If the user enters an empty string, use continue.
# while True:
#     password=input("Enter your password")
#     if password=="chetan":
#         print("Croorect Password")
#         break
#     elif password=="" or '':
#         print("Password cannot be empty. Try again.")
#         continue
#     else:
#         print(" Wrong Password. Try again.")




# Print numbers 1–30
# Skip multiples of 3 using continue,
# Stop the loop if the number is 25 using break.

# for i in range(1,31):
#     if i%3==0:
#         continue
#     if i==25:
#         break
#     print(i)