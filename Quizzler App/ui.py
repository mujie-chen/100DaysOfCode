from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

	def __init__(self, quiz_brain: QuizBrain): # ensure quiz_brain generated in main is of type QuizBrain
		self.quiz = quiz_brain

		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(bg=THEME_COLOR,padx=20,pady=20)

		self.score = 0
		self.score_label = Label(text=f"Score = {self.score}",fg="white",bg=THEME_COLOR)
		self.score_label.grid(column=1,row=0)

		self.canvas = Canvas(width=300, height=250,bg="white")
		self.question_text = self.canvas.create_text(
			150, 
			125,
			text="Text Here",
			font=("Arial",20,"italic"),
			fill="black",
			width=280 # wraps text
			)
		self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

		true_image = PhotoImage(file="images/true.png")
		self.true_button = Button(image=true_image,highlightthickness=0)
		self.true_button.grid(column=0,row=2)

		false_image = PhotoImage(file="images/false.png")
		self.false_button = Button(image=false_image,highlightthickness=0)
		self.false_button.grid(column=1,row=2)

		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		q_text = self.quiz.next_question # returns escaped question
		self.canvas.itemconfig(self.question_text, text=q_text)
