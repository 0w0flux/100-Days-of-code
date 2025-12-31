import tkinter

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WIDTH = 600
HEIGHT = 400
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def restart_timer():
    global reps, timer
    if timer:
        screen.after_cancel(timer) 
    timer = None
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00:00")
    check_marks_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN 
    short_break_sec = SHORT_BREAK_MIN 
    long_break_sec = LONG_BREAK_MIN 
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)  
    elif reps % 2 == 0:
        count_down(short_break_sec)    
        title_label.config(text="Break", fg=PINK)  
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN) 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(total_seconds):
    global timer
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=time)
    print(hours, minutes, seconds)

    if total_seconds > 0:
        timer = screen.after(1000, count_down, total_seconds - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            work_sessions = reps // 2
            marks = "✔" * work_sessions
            check_marks_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":
    screen = tkinter.Tk()
    screen.title("Pomodoro")
    screen.config(padx=100, pady=50, bg=YELLOW)

    title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    title_label.grid(column=1, row=0)

    canvas = tkinter.Canvas(width=240, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = tkinter.PhotoImage(file="Day_28/tomato.png")
    canvas.create_image(120, 112, image=tomato_img) 

    timer_text = canvas.create_text(120, 130, text="00:00:00", fill="white", font=(FONT_NAME, 20, "bold"))
    canvas.grid(column=1, row=1)

    start_button = tkinter.Button(text="Start", highlightthickness=0, command=start_timer)
    start_button.config(padx=10)
    start_button.grid(column=0, row=2)

    restart_button = tkinter.Button(text="Restart", highlightthickness=0, command=restart_timer)
    restart_button.config(padx=10)
    restart_button.grid(column=2, row=2)

    quit_button = tkinter.Button(text="Quit", highlightthickness=0, command=screen.destroy)
    quit_button.config(padx=10)
    quit_button.grid(column=1, row=4)

    check_marks_label = tkinter.Label(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
    check_marks_label.grid(column=1, row=3, sticky="n")

    screen.mainloop()