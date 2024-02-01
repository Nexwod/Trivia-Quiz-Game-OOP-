#
import data

from question_model import Question
from quiz_brain import QuizBrain

new_que = []

for i in data.question_data:
    new_que.append(Question(i['question'], i["correct_answer"]))

quiz = QuizBrain(new_que)

while quiz.still_has_question():
    quiz.next_question()


print("Thats the end of the quiz")
print(f"Your total score is {quiz.score}/{len(new_que)-1}")
