import pandas

# Todo: create csv, import how many of each colored (red, orange, black) squirrel there are

def main():
    pandas_func()
    create_csv()
    
def pandas_func():
    global file
    file = pandas.read_csv("Day_25_(intro_pandas)/intro/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

def get_color(color):
    gray = (file["Primary Fur Color"] == "Gray").sum()
    black = (file["Primary Fur Color"] == "Black").sum()
    red = (file["Primary Fur Color"] == "Cinnamon").sum()

    if color == "gray":
        return gray 
    elif color == "black":
        return black
    elif color == "red":
        return red

def create_csv():
    data_dict = {
        "color": ["gray", "black", "red"],
        "number": [get_color("gray"), get_color("black"), get_color("red")]
    }
    analyse = pandas.DataFrame(data_dict)
    analyse.to_csv("Day_25_(intro_pandas)/intro/Squirrel_Analysis.csv")


if __name__ == "__main__":
    main()
