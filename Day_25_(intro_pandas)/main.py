import pandas
import turtle


def question():
    answer_country = screen.textinput(title=f"{len(correct_guesses)} / 45 countries", prompt="What's another country's name?")
    return answer_country

def open_coordinates(country):
    country = country.strip()
    line = file[file["country"] == country]
    if not line.empty:
        return line.iloc[0] # gets the data of the row
    return None

def write_on_screen(country):
    if country is None:
        return
    writer.goto(country["x"], country["y"]) 
    writer.write(country["country"])
    screen.update()

def exit():
    '''for i in open_countries():
        if i not in correct_guesses:
            not_guessed_countries.append(i)'''
    # Its the same just with list comprehension
    not_guessed_countries = [i for i in open_countries() if i not in correct_guesses]

    write_not_guessed_countries = pandas.DataFrame(not_guessed_countries)
    write_not_guessed_countries.to_csv("Day_25_(intro_pandas)/not_guessed_countries.csv")

    print("The countries you didnt guess in: not_guessed_countries.csv")

def main():
    global score
    guessed_country = question()
    if guessed_country is None:
        return
    elif guessed_country == "exit":
        exit()
        return
    guessed_country = guessed_country.title()

    if guessed_country in countries and guessed_country not in correct_guesses:
        score += 1
        print(f"Correct answer! Score: {score}")
        correct_guesses.append(guessed_country)
        coords = open_coordinates(guessed_country)
        write_on_screen(coords)
    else:
        if guessed_country in correct_guesses:
            print("Already guessed!")
        else:
            print("Wrong answer!")
    
    screen.ontimer(main, 100)

def open_countries():
    global file
    file = pandas.read_csv("Day_25_(intro_pandas)/europe_coordinates.csv") # not 100% correct coordinates
    return file["country"].to_list()
    
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.title("Guess the countries in and around Europe")
    screen.setup(769, 512)
    image = "Day_25_(intro_pandas)/europe.gif"
    screen.bgpic(image)
    screen.tracer(0)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.speed(0)
    writer.color("red")

    countries = open_countries()
    screen.update()
    correct_guesses = []
    not_guessed_countries = []
    score = 0
    main()

    screen.exitonclick()