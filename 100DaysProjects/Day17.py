#Day 17 Project: Quiz Game

from Extra_Data.Data17.question_model import Question
from Extra_Data.Data17.data import question_data
from Extra_Data.Data17.quiz_brain import QuizBrain

question_bank = []

for questions_in_data in question_data:
    new_question = Question(questions_in_data["text"],questions_in_data["answer"])
    question_bank.append([new_question.text, new_question.answer])

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()


print(f"You've Completed the quiz. \nYour final score was: {quiz.score}/{quiz.question_number}")





