import tkinter
from tkinter import messagebox
import random
import pyperclip
import json


WIDTH = 200
HEIGHT = 200
EXPORT_PATH = "Day_30/Passwords.json"
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
    global new_data
    if not website_var.get():
        messagebox.showerror(title="Error", message="No Website entered!")
        return
    if not user_name_var.get():
        messagebox.showerror(title="Error", message="No User name entered!")
        return
    if not password_var.get():
        messagebox.showerror(title="Error", message="No Password entered!")
        return

    website = website_var.get().lower()
    user_name = user_name_var.get()
    password = password_var.get()

    new_data = {
        website: {
            "Email": user_name,
            "Password": password,   
        }
    }

    try:
        with open(EXPORT_PATH, "r") as file:
            data = json.load(file)
            data.update(new_data)

    except FileNotFoundError:
        print("File not found")
        with open(EXPORT_PATH, "w") as file:
            json.dump(new_data, file, indent=4) 
        print("New file created!")

    except json.decoder.JSONDecodeError:
        with open(EXPORT_PATH, "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open(EXPORT_PATH, "w") as file:
            json.dump(data, file, indent=4)
            print("File updated!")
    finally:
        website_var.set("")
        user_name_var.set("example@gmail.com")
        password_var.set("")

def search_file():
    try:
        website = website_var.get()
        with open(EXPORT_PATH, "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found!")

    else:    
        if website in data:
            email = data[website]["Email"]
            password = data[website]["Password"]
            messagebox.showinfo(title=website, message=f"Email/Username: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="Website not found!")

    
        

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

    website_entry = tkinter.Entry(textvariable=website_var, width=47, highlightthickness=0)
    website_entry.grid(column=1, row=1, sticky="w")
    website_entry.focus()

    website_button = tkinter.Button(text="Search Website", width=25, command=search_file, highlightthickness=0)
    website_button.grid(column=2, row=1)


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
