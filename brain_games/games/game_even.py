from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    rand_min = 1
    rand_max = 100
    question = randint(rand_min, rand_max)
    answer = "no" if question % 2 else "yes"
    return str(question), answer
