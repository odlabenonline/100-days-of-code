# ######### CONDITIONAL STATEMENT ###########
# #Don't change the code below
# number = int(input("Which number do you want to check"))
# #Don't change the code above
#
# #Write your code below this line
# if number % 2 == 0:
#     print(f"The number you entered is {number} and it is EVEN")
#     age = int(input("What is your age? "))
#     if age < 12:
#         bill = 5
#         #print("Child tickets are $5.")
#     elif age <= 18:
#         bill = 7
#         #print("Youth tickets are $7.")
#     else:
#         bill = 12
#         #print("Adult tickets are $12.")
#
#     wants_photo = input("Do you want a photo taken? Y or N")
#     if wants_photo == "Y":
#         bill += 3
#         print(f"Your final bill is ${bill}")
#     else:
#         print(f"The final bill is ${bill}")
# else:
#     print(f"The number you entered is ${number} and it is ODD")
#

# ########### BMI with INTERPRETATION ########################
# #Don't change the code below
# height = float(input("Enter your heigh in m: "))
# weight = float(input("Enter your weight in kg: "))
# #Don't change the code above

# #Write your code below this line
# bmi = round(weight / height ** 2, 2)
# if bmi < 18.5:
#     print(f"Your BMI is {bmi} and you are UNDERWEIGHT")
# elif bmi < 25:
#     print(f"Your BMI is {bmi} and you have NORMAL WEIGHT")
# elif bmi < 30:
#     print(f"Your BMI is {bmi} and you are OVERWEIGHT")
# elif bmi < 35:
#     print(f"Your BMI is {bmi} and you are OBESE")
# else:
#     print(f"Your BMI is {bmi} and you are CLINICALLY OBESE")


# # #################### LEAP YEAR CHALLENGE #######################
# # #Don't change the code below
# # year = int(input("Which year do you want to check"))
# # #Don't change the code above
# #
# # #Write your code below this line
# # if year % 4 == 0 and year % 100 != 0:
# #     print("The Year is a leap year")
# # elif year % 4 ==0 and year % 100 == 0 and year % 400 == 0:
# #     print("The year is a leap year")
# # else:
# #     print("Year is not a Leap Year!")


#################### PIZZA ORDER PROGRAMME #######################
#Don't change the code below
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want perpperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
#Don't change the code above

#Write your code below this line
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")