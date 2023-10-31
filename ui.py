from quiz_brain import QuizBrain
from tkinter import *

THEME_COLOR = "#375362"


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
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(row=2, column=1)

        self.window.mainloop()

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            question_str = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question_str, fill=THEME_COLOR)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.", fill=THEME_COLOR)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_next_question)

    def change_background(self):
        self.canvas.config(bg="Green")


