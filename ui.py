from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,
                 quiz_brain: QuizBrain):  # Here this parameter is telling us that is actually a QuizBrain object since we want to get data from another class using an existing object
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.points = Label(text=f"Score: {self.quiz.score}", font=("Arial", 15, "normal"), pady=20, fg="white", bg=THEME_COLOR)
        self.points.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="Questions here", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR,
                                                width=280)  # setting width so the text can get wrapped into our canvas

        self.true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_image, command=self.check_true_button, highlightthickness=0,
                                  highlightbackground=THEME_COLOR)
        self.true_button.grid(column=0, row=2)
        self.false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_image, command=self.check_false_button, highlightthickness=0,
                                   highlightbackground=THEME_COLOR)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(
            self):  # Since we pass a QuizBrain as a parameter now in this method, we can use it to get hold of its next_question method, which returns a question
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the trivia")
            self.reset_bg()
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_true_button(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.get_next_question()

    def check_false_button(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        self.get_next_question()

    def reset_bg(self):
        self.canvas.configure(bg="white")

    def give_feedback(self, result):
        if result:
            self.canvas.configure(bg="green")
            self.points.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.configure(bg="red")
        self.canvas.after(1000, self.reset_bg)
