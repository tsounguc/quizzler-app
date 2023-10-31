from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
from tkinter import *


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("Arial", 12, "normal"), bg=THEME_COLOR, foreground="White")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=self.quiz.next_question(),
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.get_next_question)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.get_next_question)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def get_next_question(self):
        question_str = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question_str)



