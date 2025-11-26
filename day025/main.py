# # # # with open("weather_data.csv") as data_file:
# # # #     data = data_file.readlines()
# # # #     print(data)
# # #
# # # import csv
# # #
# # # with open("weather_data.csv") as data_file:
# # #     data = csv.reader(data_file)
# # #     temperatures =[]
# # #     for row in data:
# # #         if row[1] != "temp":
# # #             temperatures.append(row[0])
# # #     print(temperatures)
# # #
# import pandas #really powerful tool needs to be installed cos is not inbuilt
#
# data = pandas.read_csv("weather_data.csv") #Get hold of the data
# # # print(data)
# # # print(type(data))
# # # print(data["temp"])
# # # print(type(data["temp"]))
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# #
# # average_list = sum(temp_list) / len(temp_list)
# # print(data["temp"].mean())
# #
# # print(data["temp"].max())
# # print(data["temp"].min())
# #
# # print(data["condition"])
# ########### Dealing with rows #############
# #Get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# #
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)
#
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")




######### SQUIRREL DATA ANALYSIS ###########

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251125.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")