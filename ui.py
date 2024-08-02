from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Interface():
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.window = Tk()
        self.question = quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background = THEME_COLOR)

        # Label
        self.score_text = Label(text = f"Score: ", bg = THEME_COLOR, fg = "white", font=("Arial", 12, "bold"))
        self.score_text.grid(row=0, column=1, sticky="ew")

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text = "Some Question Text", fill = "black", font = ("Arial", 15, "italic"), width=280)
        self.canvas.grid(row=1, column=0, sticky="ew", columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file = "images/true.png")
        false_img = PhotoImage(file = "images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.user_true_answer).grid(row = 2, column = 0)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.user_false_answer).grid(row = 2, column = 1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg = "white")
        self.score_text.config(text= f"Score: {self.question.score}")
        q_text = self.question.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)

    def user_true_answer(self):
        self.give_feedback(self.question.check_answer("True"))
        
    def user_false_answer(self):
        self.give_feedback(self.question.check_answer("False"))

    def give_feedback(self, answer):
        self.canvas.config(background='green') if answer == True else self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)
        