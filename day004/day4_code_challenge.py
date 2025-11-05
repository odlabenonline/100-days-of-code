# # # #Write your code below this line
# # # #Hint: Remember to import the random module first
# # #
# # # import random
# # #
# # # random_side = random.randint(0,1)
# # # if random_side == 1:
# # #     print("Heads")
# # # else:
# # #     print("Tails")
# #
# #
# # ########### Who buys the meal ###############
# # import random
# # #Split string method
# # names_string = input("Give me everybody's names, separated by a comma.")
# # names = names_string.split(",")
# # # Don't change the code above
# #
# # # Write you code below this line
# # num_items = len(names)
# # random_choice = random.randint(0, num_items - 1)
# # person_who_will_pay = names[random_choice]
# # print(person_who_will_pay + " is the person who is going to pay today1")
# #
# # #The Code above could also be simplified as this
# # #print(names[random.randint(0,len(names)-1)])
# # #print(len(names))
# #
# # #PYTHON actually provides a module to help with such a situation as scripted below with far less code.
# # person_who_will_pay = random.choice(names)
# # print(person_who_will_pay + "is going to buy the meal today!")
#
# ############ TREASURE MAP Coding Challenge ###################
# # Don't change the code below
# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
#
# # Don't change the code above
#
# #Write your code below this row
# horizonal = int(position[0])
# vertical =int( position[1])
#
# selected_row = map[vertical - 1]
# selected_row[horizonal - 1] = "X"
#
# print(f"{row1}\n{row2}\n{row3}")





############# ROCK PAPER SCISSORS GAME ###############
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 2 for paper or 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed in an invalid number")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print(f"Computer chose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("you lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")
