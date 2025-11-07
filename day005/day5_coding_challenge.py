# # # #Write a program that calculates the average student height from a list of heights
# # # # Don't change the code below
# # # student_heights = input("Input a list of students heights ").split()
# # # for n in range(0, len(student_heights)):
# # #     student_heights[n] = int(student_heights[n])
# # # print(student_heights)
# # # # Don't change the code above
# # #
# # # # #Write your code below this row
# # # # total_height = sum(student_heights)
# # # # number_of_students = len(student_heights)
# # # # average_ht = round(total_height/number_of_students)
# # # # print(average_ht)
# # #
# # # #The above code works alright but we want to make use of the FOR LOOP
# # #
# # # total_height = 0
# # # for height in student_heights
# # #     totalheight += height
# # # #print(total_height)
# # #
# # # number_of_students = 0
# # # for student in student_heights
# # #     number_of_students += 1
# # # #print(number_of_students)
# # #
# # # average_height = round(total_height/number_of_students)
# # # print(average_height)
# # #
# # #
# # # total = 0
# # # for number in range(1,101):
# # #     total += number
# # # print(total)
# #
# #
# #
# # # ################## Adding EVENS in a range ##################
# # # # Don't change the code below
# # # student_scores = input("Input a list of student scores").split()
# # # for n in range(0, len(student_scores)):
# # #     student_scores[n] = int(student_scores[n])
# # # print(student_scores)
# # # # Don't change the code above
# #
# # # #Write your code below this row
# # total = 0
# # for number in range(1, 101, 2): #The two is called step size
# #     total += number
# # print(number)
#
# ########### FizzBuzz ###############
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 ==0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Fizz")
#     elif number % 3 == 0:
#         print("Buzz")
#     else:
#         print("number")


################## PASSWORD GENERATOR ##########################
import random
letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password"\n))
nr_symbols = int(input("How many symbols would you like"\n))
nr_numbers = int(input("How many numbers would you like"\n))

#Eazy Level (Sequenced LettersSymbolsNumbers



#Hard Level (RandomizedMixed)