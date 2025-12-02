# # # Review:
# # # Create a function called greet().
# # # Write 3 print statements inside the function.
# # # Call the greet() function and run your code.
# #
# # # #Simple Function
# # # def greet():
# # #     print("Hello World")
# # #     print("I just created a function")
# # #     print("...and I called it to execute; Thanks!")
# # #
# # # greet()
# #
# #
# # #Function that allows for input
# #
# # def greet_with_name(name): # Name in the function as a data type is a parameter and the value passed when called is argument
# #     print(f"Hello {name}")
# #     print(f"How do you do {name}")
# #
# # name = input("Please what is your name: \n")
# # greet_with_name(name)
# # from Day003.day3_love_calculator import name1
#
#
# #Functions with more than 1 input
# def greet_with(name, location):
#     print(f"hello {name}")
#     print(f"What is it like in {location}")
#
# name = input("Please enter your name\n")
# location = input("Please enter your city\n")
#
# greet_with(name, location)

#Functions with Keyword Arguments
def greet_with(name, location):
    print(f"hello {name}")
    print(f"What is it like in {location}")

username = input("Please enter your name\n")
city = input("Please enter your city\n")

greet_with(location = city, name = username) #Keyword Arguments, position doesn't matter
