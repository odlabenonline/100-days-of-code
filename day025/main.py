# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[0])
#     print(temperatures)
#
import pandas #really powerful tool needs to be installed cos is not inbuilt

data = pandas.read_csv("weather_data.csv") #Get hold of the data
print(data)
print(type(data))
print(data["temp"])
print(type(data["temp"]))