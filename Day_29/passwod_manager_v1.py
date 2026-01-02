import tkinter
from tkinter import messagebox
import pandas
import random
import pyperclip


WIDTH = 200
HEIGHT = 200
characters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '0','1','2','3','4','5','6','7','8','9',
]
special_chars = [
    '!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',';',':',',','.','<','>','/','?','|','~'
]

def generate_password():
    password_list = []
    for i in range(8):
        rnd = random.choice(characters)
        password_list.append(rnd)
        rnd = random.choice(special_chars)
        password_list.append(rnd)

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_var.set(password)
    pyperclip.copy(password)

def save_password():
    if not website_var.get():
        messagebox.showerror(title="Error", message="No Website entered!")
    elif not user_name_var.get():
        messagebox.showerror(title="Error", message="No User name entered!")
    elif not password_var.get():
        messagebox.showerror(title="Error", message="No Password entered!")

    else:
        is_okay = messagebox.askokcancel(title="These are the details entered:", message=f"Website: {website_var.get()} \nUser name: {user_name_var.get()} \nPassword: {password_var.get()} \n\nIs it okay to save?")
        if is_okay:
            print("worked")
            create_csv(website_var.get(), user_name_var.get(), password_var.get())

        website_var.set("")
        user_name_var.set("example@gmail.com")
        password_var.set("")

def create_csv(website, user_name, password):
    data_dict = {
        "url": [website],
        "username": [user_name],
        "password": [password]
    }
    passwords = pandas.DataFrame(data_dict)
    passwords.to_csv("Day_29/Passwords.csv", mode="a", header=False, index=False)

if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.title("Python Password Manager")
    screen.config(padx=20, pady=20)

    website_var = tkinter.StringVar()
    user_name_var = tkinter.StringVar()
    password_var = tkinter.StringVar()

    canvas = tkinter.Canvas(width=WIDTH, height=HEIGHT, highlightthickness=0)
    logo_img = tkinter.PhotoImage(file="Day_29/logo.png")
    canvas.create_image(WIDTH / 2, HEIGHT / 2, image=logo_img)
    canvas.grid(column=0, row=0, columnspan=3)

    website_frame = tkinter.Frame(screen)
    website_frame.grid(column=0, row=1, sticky="w")
    website_label = tkinter.Label(website_frame, text="Website:", highlightthickness=0)
    website_label.pack(side="left")
    website_star = tkinter.Label(website_frame, text="*", fg="red")
    website_star.pack(side="left")

    website_entry = tkinter.Entry(textvariable=website_var, width=77, highlightthickness=0)
    website_entry.grid(column=1, row=1, columnspan=2)
    website_entry.focus()

    email_frame = tkinter.Frame(screen)
    email_frame.grid(column=0, row=2, sticky="w")
    user_name_label = tkinter.Label(email_frame, text="Email/Username:", highlightthickness=0)
    user_name_label.pack(side="left")
    user_name_star = tkinter.Label(email_frame, text="*", fg="red")
    user_name_star.pack(side="left")

    user_name_entry = tkinter.Entry(textvariable=user_name_var, width=77, highlightthickness=0)
    user_name_entry.grid(column=1, row=2, columnspan=2)
    user_name_entry.insert(0, "example@gmail.com")

    password_frame = tkinter.Frame(screen)
    password_frame.grid(column=0, row=3, sticky="w")
    password_label = tkinter.Label(password_frame, text="Password:", highlightthickness=0)
    password_label.pack(side="left")
    password_star = tkinter.Label(password_frame, text="*", fg="red")
    password_star.pack(side="left")

    password_entry = tkinter.Entry(textvariable=password_var, width=47, highlightthickness=0)
    password_entry.grid(column=1, row=3, sticky="w")

    password_button = tkinter.Button(text="Generate Password", width=25, command=generate_password, highlightthickness=0)
    password_button.grid(column=2, row=3, sticky="w")

    add_button = tkinter.Button(text="Add", command=save_password, highlightthickness=0)
    add_button.grid(column=1, row=4, columnspan=2, sticky="we")

    screen.mainloop()
