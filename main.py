# # with open ("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # # print(type(data))
# # # print(data["temp"])
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # # print(sum(temp_list)/len(temp_list))
# # print(data["temp"].mean())
# # print(data["temp"].max())
# # # Same thing
# # print(data["condition"])
# # print(data.condition)
#
# # Get data in row
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # print(monday.condition)
# # print(monday.temp[0] * 9/5 + 32)
#
# # Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]
cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
data_dict = {
    "color": ["gray", "black", "cinnamon"],
    "number": [len(gray), len(black), len(cinnamon)]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrels_count.csv")