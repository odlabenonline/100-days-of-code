# Making update to the day09 (review)
# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again", #always cap off your entries with a comma
# }
#
# # To retrieve an item from a dictionary; similar to in list
# # NOTE dictionary items are and selected with a key
# # The key used in retrieving must match the key used in the dictionary
# print(programming_dictionary["Bug"]) #A common error called "KeyError" comes from wrongly requested key eg. Bog
#
# #Adding New Items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)
#
# #Create an empty dictionary
# empty_dictionary = {}
#
# #Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
#
# #Edit an item in a dictionary
# programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)
#
# #Loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])
#
#Nesting List in a Dicitionary
capitals = {
    #"France": "Paris", "Lille", "Dijon" (This won't work till we make France a list of cities as shown below
    "France":["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],

}

#you can also have a list in a list as shown below
list1 = ["A", "B", ["C", "D"]]

#Nesting a Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 14},

}

#Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },

    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 14
    },
]