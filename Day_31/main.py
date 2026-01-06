import tkinter
import pandas
import random

WIDTH = 900
HEIGHT = 600
BACKGROUND_COLOR = "#B1DDC6"
TOP_500_WORDS_FILE_PATH = "Day_31/top_500_words_spanish_to_german.csv"

def flip_card():
    canvas.itemconfig(card_img, image=BACK_IMG)
    canvas.itemconfig(word_label, text=data_dict["German"])
    canvas.itemconfig(language_label, text="German")

def change_word():
    global data_dict
    if not data_dict_list:
        canvas.itemconfig(word_label, text="There is nothing left to learn!")
        canvas.itemconfig(language_label, text="")
        return
    
    data_dict = random.choice(data_dict_list)
    canvas.itemconfig(card_img, image=FRONT_IMG)
    canvas.itemconfig(word_label, text=data_dict["Spanish"])
    canvas.itemconfig(language_label, text="Spanish")
    screen.after(3000, flip_card)

def right_pressed():
    global right_count
    right_count += 1
    data_dict_list.remove(data_dict)
    change_word()

def wrong_pressed():
    global wrong_count
    wrong_count += 1

    df = pandas.DataFrame([{k: v.strip() for k, v in data_dict.items()}])
    df.to_csv(
        "Day_31/words_to_learn.csv", "a", index=False, header=not pandas.io.common.file_exists("Day_31/words_to_learn.csv"), sep=",")
    change_word()

if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.title("Flash Card App | Capstone Project")
    screen.config(padx=50, pady=50, background=BACKGROUND_COLOR)

    FRONT_IMG = tkinter.PhotoImage(file="Day_31/images/card_front.png")
    BACK_IMG = tkinter.PhotoImage(file="Day_31/images/card_back.png")
    RIGHT_IMG = tkinter.PhotoImage(file="Day_31/images/right.png")
    WRONG_IMG = tkinter.PhotoImage(file="Day_31/images/wrong.png")

    right_count = 0
    wrong_count = 0

    data = pandas.read_csv(TOP_500_WORDS_FILE_PATH)
    data_dict_list = data.to_dict(orient="records")
    data_dict = {}

    canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, highlightthickness=0, bg=BACKGROUND_COLOR)
    card_img = canvas.create_image(WIDTH / 2, HEIGHT / 2, image=FRONT_IMG)
    language_label = canvas.create_text(WIDTH / 2, HEIGHT / 2 - 100, text="", fill="black", font=("Arial", 25, "italic"))
    word_label = canvas.create_text(WIDTH / 2, HEIGHT / 2, text="", fill="black", font=("Arial", 50, "bold"))

    right_button = tkinter.Button(image=RIGHT_IMG, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR, command=right_pressed)
    wrong_button = tkinter.Button(image=WRONG_IMG, highlightthickness=0, border=0, activebackground=BACKGROUND_COLOR, command=wrong_pressed)

    canvas.grid(column=0, row=0, columnspan=2)
    right_button.grid(column=1, row=1)
    wrong_button.grid(column=0, row=1)

    change_word()
    screen.mainloop()
