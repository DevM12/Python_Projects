from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

def quiz_game():
    def question_bank_creator(questions):
        questions_bank=[]
        for question in questions:
            question_text=question['text']
            question_answer=question['answer']
            new_question=Question(question_text,question_answer)
            questions_bank.append(new_question)
        return questions_bank

    question_bank=question_bank_creator(question_data)
    quiz=QuizBrain(question_bank)
    quiz.next_question()


quiz_game()