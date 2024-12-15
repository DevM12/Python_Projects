import random

class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def next_question(self):
        def answer_check(ques,num):
            answer = input(f'Q.{num}: {ques.text} (True/False)').strip().title()
            if ques.answer == answer:
                self.score += 1
                print(f'You got it right! \nYour score is:{self.score}/{self.question_number}')

            else:
                print(f'You got it wrong! \nYour score is:{self.score}/{self.question_number}')

        for questions in self.question_list:
            new_question=questions
            self.question_number+=1
            answer_check(new_question,self.question_number)

        print(f'\n\nThank you for completing the quiz \nYour final score is: {self.score}/{self.question_number}')