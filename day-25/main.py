import pandas

with open("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv") as data:
    file = pandas.read_csv(data)
    color_list = file["Primary Fur Color"].to_list()
    cinnamon = 0
    black = 0
    gray = 0
    for i in color_list:
        if i == "Cinnamon":
            cinnamon += 1
        elif i == "Gray":
            gray += 1
        elif i == "Black":
            black += 1
        else:
            pass
    data_dict = {"Fur Color": ["Cinnamon", "Black", "Gray"], "Count": [cinnamon, black, gray]}
    convertor = pandas.DataFrame(data_dict)
    convertor.to_csv("New_data.csv")
