from tkinter import *

THEME_COLOR = "#375362"

class Interface():
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background = THEME_COLOR)

        # Label
        self.score_text = Label(text = "Score: ", bg = THEME_COLOR, fg = "white", font=("Arial", 12, "bold"))
        self.score_text.grid(row=0, column=1, sticky="ew")

        # Canvas
        canvas = Canvas(height=250, width=300, bg="white")
        canvas.create_text(150, 125, text = "Some Question Text", fill = "black", font = ("Arial", 20, "italic"))
        canvas.grid(row=1, column=0, sticky="ew", columnspan=2, pady=50)

        # Buttons
        true_img = PhotoImage(file = "images/true.png")
        false_img = PhotoImage(file = "images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0).grid(row = 2, column = 0)
        self.false_button = Button(image=false_img, highlightthickness=0).grid(row = 2, column = 1)

        self.window.mainloop()

quiz_interface = Interface()