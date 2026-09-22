import tkinter
from tkinter import ttk

def main():
    global label_03, input
    frame = ttk.Frame(screen, padding=10)
    frame.grid()
    
    input = tkinter.Entry(frame, width=10)
    input.grid(column=1, row=0, padx=5)
    
    label_01 = ttk.Label(frame, text="Miles")
    label_01.grid(column=2, row=0, padx=5)
    
    label_02 = ttk.Label(frame, text="is equal to")
    label_02.grid(column=0, row=1)

    label_03 = ttk.Label(frame, text="0")
    label_03.grid(column=1, row=1)

    label_04 = ttk.Label(frame, text="Km")
    label_04.grid(column=2, row=1)

    button_01 = ttk.Button(frame, text="Calculate", command=calculate)
    button_01.grid(column=1, row=2)

    button_02 = ttk.Button(frame, text="Quit", command=screen.destroy)
    button_02.grid(column=1, row=3)

def calculate():
    global label_03
    label_03.config(text=f"{round(float(input.get())*1.609344, 2)}")

if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.title("Mile to Km converter")
    screen.minsize(width=200, height=200)
    screen.config(padx=20, pady=20)

    main()

    screen.mainloop()




