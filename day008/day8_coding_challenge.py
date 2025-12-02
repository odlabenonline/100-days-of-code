#Write your code below this line
import math

def paint_cal(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area/cover)
    print(f"You'll need {num_of_cans}")

test_h = int(input("height of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_cal(height = test_h, width = test_w, cover = coverage)


# # #Write your code below this line
# # import math
# # def paint_calc(height, width, cover):
# #     cans = math.ceil((height * width)/5)
# #     print(f"You will need {cans} can(s) to finish painting")
# #
# #
# # #Write your code above this line
# #
# # #Don't change the code below
# # test_h = int(input("Height of wall: \n"))
# # test_w = int(input("Width of wall: \n"))
# # coverage = 5
# # paint_calc(height = test_h, width = test_w, cover = coverage)
#
# ########### PRIME NUMBER CHECKER ###########
# #Number that is only divisible by 2 numbers, 1 and the number itself
# #Write your code below this line
#
# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number")
#     else:
#         print("It's not a prime number")
#
# #It's a prime number.
# #It's not a prime  number.
#
#
# #Write your code above this line
#
# #Do NOT change any of the code below
# n = int(input("Check this number: "))
# prime_checker(number=n)
