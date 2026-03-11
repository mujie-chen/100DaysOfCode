import os
import requests
from tkinter import *
os.chdir('/Users/mujiechen/Library/CloudStorage/Dropbox/Courses/100 Days of Code/Quizzler App')
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# edit next_question() definition to convert current_question.text using html.unescape()
# replace user_answer, capture question as output that QuizInterface() calls
from ui import QuizInterface

THEME_COLOR = "#375362"

# get question bank from database using API call (goes into data.py)
parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"] # replaces here but just make visible

# logic from Day 17 quiz app
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# ui setup as a class (from ui.py)
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
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
    		fill=THEME_COLOR,
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
        q_text = self.quiz.next_question() # returns escaped question
        self.canvas.itemconfig(self.question_text, text=q_text)

# creating an object from the imported QuizInterface class
quiz_ui = QuizInterface(quiz) # passes Question, including next_question, to QuizInteraface
# next_question passed from main.py, not actually in ui.py


# while quiz.still_has_questions():
#    quiz.next_question()
# cannot have mainloop running within another while loop

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


