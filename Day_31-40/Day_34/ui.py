import tkinter 
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FALSE_IMG = "Day_34/images/false.png"
TRUE_IMG = "Day_34/images/true.png"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.screen = tkinter.Tk()
        self.screen.title("Quiz")
        self.screen.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = tkinter.Label(self.screen, text="Score: 0", fg="white", background=THEME_COLOR, font=("Arial", 15))
        self.score_label.grid(row=0, column=1)
        self.score_label.config(padx=20, pady=20)

        self.canvas = tkinter.Canvas(self.screen, width=300, height=250, bg="white", highlightthickness=0)
        self.question_label = self.canvas.create_text(150, 125, text="This is a label spanning two columns", width=284, font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=10, pady=25)

        true_img = tkinter.PhotoImage(file=TRUE_IMG)
        false_img = tkinter.PhotoImage(file=FALSE_IMG)

        self.true_button = tkinter.Button(image=true_img, command=lambda: self.give_feedback(self.quiz.check_answer("true")), highlightthickness=0, border=0, activebackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0, padx=10, pady=20)

        self.false_button = tkinter.Button(image=false_img, command=lambda: self.give_feedback(self.quiz.check_answer("false")), highlightthickness=0, border=0, activebackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1, padx=10, pady=20)


        self.get_next_question()
        self.screen.mainloop()

    def get_next_question(self):
        self.screen.config(bg=THEME_COLOR)
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=question_text)
        else:
            self.score_label.config(text="")
            self.canvas.itemconfig(self.question_label, text=f"You have reached the end of the quiz! \nYour score:{self.quiz.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right == True:
            self.screen.config(bg="green")
        else:
            self.screen.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.screen.after(500, self.get_next_question)