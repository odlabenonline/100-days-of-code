# #List is a data structure that helps keep group pieces with connection with each other.
# #Variables won't help with such data and as such LIST helps
# #When you also need order of items then LIST helps as a good data structure.
#
# #SYNTAX         fruits = [item1, item]
# #.append is used to add to a list apped(x)
# #Other functions are extend(), insert(), pop(), remove(),
# fruits = ["cherry", "Apple", "pear"]
#
# states_of_america = [
#     "Delaware",          # 1st - December 7, 1787
#     "Pennsylvania",      # 2nd - December 12, 1787
#     "New Jersey",        # 3rd - December 18, 1787
#     "Georgia",           # 4th - January 2, 1788
#     "Connecticut",       # 5th - January 9, 1788
#     "Massachusetts",     # 6th - February 6, 1788
#     "Maryland",          # 7th - April 28, 1788
#     "South Carolina",    # 8th - May 23, 1788
#     "New Hampshire",     # 9th - June 21, 1788
#     "Virginia",          # 10th - June 25, 1788
#     "New York",          # 11th - July 26, 1788
#     "North Carolina",    # 12th - November 21, 1789
#     "Rhode Island",      # 13th - May 29, 1790
#     "Vermont",           # 14th - March 4, 1791
#     "Kentucky",          # 15th - June 1, 1792
#     "Tennessee",         # 16th - June 1, 1796
#     "Ohio",              # 17th - March 1, 1803
#     "Louisiana",         # 18th - April 30, 1812
#     "Indiana",           # 19th - December 11, 1816
#     "Mississippi",       # 20th - December 10, 1817
#     "Illinois",          # 21st - December 3, 1818
#     "Alabama",           # 22nd - December 14, 1819
#     "Maine",             # 23rd - March 15, 1820
#     "Missouri",          # 24th - August 10, 1821
#     "Arkansas",          # 25th - June 15, 1836
#     "Michigan",          # 26th - January 26, 1837
#     "Florida",           # 27th - March 3, 1845
#     "Texas",             # 28th - December 29, 1845
#     "Iowa",              # 29th - December 28, 1846
#     "Wisconsin",         # 30th - May 29, 1848
#     "California",        # 31st - September 9, 1850
#     "Minnesota",         # 32nd - May 11, 1858
#     "Oregon",            # 33rd - February 14, 1859
#     "Kansas",            # 34th - January 29, 1861
#     "West Virginia",     # 35th - June 20, 1863
#     "Nevada",            # 36th - October 31, 1864
#     "Nebraska",          # 37th - March 1, 1867
#     "Colorado",          # 38th - August 1, 1876
#     "North Dakota",      # 39th - November 2, 1889
#     "South Dakota",      # 40th - November 2, 1889
#     "Montana",           # 41st - November 8, 1889
#     "Washington",        # 42nd - November 11, 1889
#     "Idaho",             # 43rd - July 3, 1890
#     "Wyoming",           # 44th - July 10, 1890
#     "Utah",              # 45th - January 4, 1896
#     "Oklahoma",          # 46th - November 16, 1907
#     "New Mexico",        # 47th - January 6, 1912
#     "Arizona",           # 48th - February 14, 1912
#     "Alaska",            # 49th - January 3, 1959
#     "Hawaii"             # 50th - August 21, 1959
# ]

############## NESTED LIST ################
fruits = ["strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen) #This prints two list (fruits and vegetable sin a larger list (dirty_dozens)
