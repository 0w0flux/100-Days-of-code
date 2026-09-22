import pandas


def main():
    pandas_func()
    challenge_01()
    challenge_02()
    challenge_03()
    challenge_04()
    
def pandas_func():
    global file
    file = pandas.read_csv("Day_25_(intro_pandas)/intro/weather_data.csv")

def challenge_01():
    temp = file["temp"].max()
    print(round(temp, 2))
    return temp

def challenge_02():
    print(file[file["temp"] == file["temp"].max()])

def challenge_03():
    monday = file[file["day"] == "Monday"]
    print(monday["temp"])
    print(monday["temp"] * 9/5 + 32) # in Fahrenheit

def challenge_04():
    data_dict = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data = pandas.DataFrame(data_dict)
    data.to_csv("Day_25_(intro_pandas)/intro/challenge_04.csv")

if __name__ == "__main__":
    main()
