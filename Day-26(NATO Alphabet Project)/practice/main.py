import random

#
# def add_1(num):
#     a=num+1
#     a*=2
#     return a
#
# numbers=[1,2,3,4,5]
# new_list=[add_1(n) for n in range(1,5)]
# print(new_list)

def random_score():
    score= random.randint(1,10)*10+random.randint(1,9)
    while score>100:
        score= random.randint(1,10)*10+random.randint(1,9)
    return score


names=['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
student_scores={name:random_score() for name in names}
print(student_scores)
passed_students={name:score for (name,score) in student_scores.items() if score>30}
print(passed_students)