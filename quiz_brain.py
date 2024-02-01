class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_question(self):
        return len(self.question_list) > self.question_number+1


    def next_question(self):
        self.question_number += 1
        # print(self.still_has_question())
        next_q = input(f"Q{self.question_number}. {self.question_list[self.question_number].text} (True/False)? ")
        self.check_answer(next_q=next_q, correct=self.question_list[self.question_number].answer)
    def check_answer(self, next_q, correct):
        if next_q.lower() == correct.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")

        print(f"The correct answer is {correct}")
        print(f"And your score is {self.score}/{self.question_number} \n")
        # print(next_q, correct)
