from tkinter import *
import requests


def get_quote():
    global quote_text

    response = requests.get(url="https://ap.kanye.rest")
    if response.status_code != 200:
        raise Exception(f"{response.status_code}")
    else:
        data = response.json()
        print(data)
        if len(data["quote"]) >= 50:
            canvas.itemconfig(quote_text, text=data["quote"], font=("Arial", 20, "bold"))
        else:
            canvas.itemconfig(quote_text, text=data["quote"], font=("Arial", 30, "bold"))

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="Day_33/kanye/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="Day_33/kanye/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()