#TODO: 1 ########### CODE CHALLENGE 1
# #Don't change the code below
# two_digit_number = input("Type a two digit number")
# #Dont change the code above
#
# ###################################################
# #Write your code below this line
#
# print(type(two_digit_number))
#
# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]
#
# results = int(first_digit) + int(second_digit)
# print(results)
#
#
#
#
#TODO: 2 ######## CODE CHALLENGE 2
# # Don't change the code below
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# # Don't  change the code above
#
# #Write your code below this line
#
# bmi = (float(weight) / (float(height) ** 2))
# print("Your BMI is " + str(bmi))



#TODO: 3 ########## CODING CHALLENGE 3
# # Don't change the code below
# age = input("What is your current age? ")
# # Dont change the code above
#
# #Write your code below this line
# #QUICK INFO TO GUIDE
# # 1 YEAR = 365 days
# # 1 YEAR = 52 weeks
# # 1 YEAR = 12 months
#
# age_left = 90 - int(age)
#
# days_left = int(age_left) * 365
# weeks_left = int(age_left) * 52
# months_left = int(age_left) * 12
#
# print(f"You have {days_left} days, {weeks_lef10t} weeks, and {months_left} months left")


#TODO: Final ############# Final Quiz Code Challenge #################
# Welcome to the tip calculator
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill? 7
# Each person should pay $19.93

print("Welcome to the tip calculator")
print("##############################")

bill = float(input("What was the total bill? : $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? :"))
people = int(input("How many people are to split the bill? : "))

bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person among the {people} people should pay: ${bill_per_person}")
