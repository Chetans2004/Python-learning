# #Stirng formating
# It is a process of inserting an object into a predefined string
##  (%) formating
# name="Chetan"
# age=21
# print("My name is %s and my age is %d " % (name,age))

##2.str.format
# name="Chetan"
# age=21
# print("My name is :{} and my age is  :{}".format(name,age))

##3.f-string
# name="Chetan"
# age=21
# city="Dharwad"
# print(f"My name is {name} my age is {age} and i live in {city}")

#PRACTICE QUESTIONS
#1.Write a program that asks the user for their city and pincode. Print →
# "I live in <city> and my pincode is <pincode>."
# city=input("Enter your city")
# pin_code=int(input("Enter your pincode"))
# print(f"I live in {city} and my pincode is {pin_code}")


#2Given marks = 456 and total = 500, print →
# "I scored 456 out of 500, which is 91.20%" (show percentage with 2 decimal places).
marks_i_taken=456
total_marks=500
pecentage=marks_i_taken/total_marks *100
print(f"I scored {marks_i_taken} out of {total_marks}, which is {pecentage}")




