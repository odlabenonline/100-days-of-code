# # ######### CONDITIONAL STATEMENT ###########
# # #Don't change the code below
# # number = int(input("Which number do you want to check"))
# # #Don't change the code above
# #
# # #Write your code below this line
# # if number % 2 == 0:
# #     print(f"The number you entered is {number} and it is EVEN")
# #     age = int(input("What is your age? "))
# #     if age < 12:
# #         bill = 5
# #         #print("Child tickets are $5.")
# #     elif age <= 18:
# #         bill = 7
# #         #print("Youth tickets are $7.")
# #     else:
# #         bill = 12
# #         #print("Adult tickets are $12.")
# #
# #     wants_photo = input("Do you want a photo taken? Y or N")
# #     if wants_photo == "Y":
# #         bill += 3
# #         print(f"Your final bill is ${bill}")
# #     else:
# #         print(f"The final bill is ${bill}")
# # else:
# #     print(f"The number you entered is ${number} and it is ODD")
# #

# # ########### BMI with INTERPRETATION ########################
# # #Don't change the code below
# # height = float(input("Enter your heigh in m: "))
# # weight = float(input("Enter your weight in kg: "))
# # #Don't change the code above

# # #Write your code below this line
# # bmi = round(weight / height ** 2, 2)
# # if bmi < 18.5:
# #     print(f"Your BMI is {bmi} and you are UNDERWEIGHT")
# # elif bmi < 25:
# #     print(f"Your BMI is {bmi} and you have NORMAL WEIGHT")
# # elif bmi < 30:
# #     print(f"Your BMI is {bmi} and you are OVERWEIGHT")
# # elif bmi < 35:
# #     print(f"Your BMI is {bmi} and you are OBESE")
# # else:
# #     print(f"Your BMI is {bmi} and you are CLINICALLY OBESE")


# # # #################### LEAP YEAR CHALLENGE #######################
# # # #Don't change the code below
# # # year = int(input("Which year do you want to check"))
# # # #Don't change the code above
# # #
# # # #Write your code below this line
# # # if year % 4 == 0 and year % 100 != 0:
# # #     print("The Year is a leap year")
# # # elif year % 4 ==0 and year % 100 == 0 and year % 400 == 0:
# # #     print("The year is a leap year")
# # # else:
# # #     print("Year is not a Leap Year!")


# #################### PIZZA ORDER PROGRAMME #######################
# #Don't change the code below
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want perpperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# #Don't change the code above

# #Write your code below this line
# bill = 0

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill +=2
#     else:
#         bill +=3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")


################# TREAASURE ISLAND GAME ##################
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")