# # #Simple Calculator
# # # num1=int(input("Enter first number"))
# # # num2=int(input("Enter second number"))
# # # operator=input("Enter operator (+,-,*,/):")
# # # if operator == '+':
# # #     print("result=",num1+num2)
# # # elif operator == '-':
# # #     print("Result=",num1-num2)
# # # elif operator == '*':
# # #     print("Result=",num1*num2)
# # # else:
# # #     print("Result=",num1/num2)


# # #ATM Cash Withdrawal Simulator

# # # Concepts used: nested if, multiple conditions
# # pin_number=232357
# # total_balance=100000
# # withdraw_amount=int(input("Enter the amount you want to withdraw"))
# # user_pin_number=int(input("Enter your pin number"))
# # if pin_number == user_pin_number:
# #     if withdraw_amount <= total_balance:
# #         if(withdraw_amount%100==0):
# #             print("Transaction Successful ")
# #             print("Please Collet cash")
# #             print("Ramaining balance=",total_balance-withdraw_amount)
# #         else:
# #             print("Amount should be a multiple of 100 (100, 200, 300, ...).")
# #     else:
# #           print("Insufficient balance! Please enter a smaller amount.")
# # else:
# #     print("Enter valid Pin")



# Movie Ticket Price System
# Concepts used: nested if
# Description:
# Ask for:
# Age
# Time of show (Morning/Evening)
# # Rules:
# Below 12 → ₹100
# 12–18 → ₹150
# 18+ → ₹200
# If it’s an evening show → add ₹50 extra.

# age=int(input("Enter your age"))
# show_time = input("Enter time of show (Morning/Evening): ").lower()
# print("You selected", show_time, "show.")
# if show_time == "morning":
#     if age<12:
#         print("The ticket price is 100")
#     elif age>12 and age <=18:
#         print("Ticket price is 150")
#     else:
#         print("Ticket price is 200")
# elif show_time == "evening":
#     if age < 12:
#         print("Ticket price is ₹150")  # 100 + 50
#     elif age <= 18:
#         print("Ticket price is ₹200")  # 150 + 50
#     else:
#         print("Ticket price is ₹250")  # 200 + 50

# else:
#     print("Invalid input! Please enter Morning or Evening.")

#BMI Calculator
weight=float(input("Enter your weight in KG"))
height=float(input("Enter your height in meter"))

bmi = weight / (height ** 2)
print(bmi)
if bmi <=18.4:
    print("You are in Under weight")
elif bmi >=18.5 and bmi <24.9:
       print("You are in Normal weight")
else:
    print("You are in over weight")