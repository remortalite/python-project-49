from random import randint


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_SIZE = 10


def censor_progression(progression):
    rand_idx = randint(0, len(progression) - 1)
    correct_el = progression[rand_idx]
    progression[rand_idx] = None
    return progression, correct_el


def make_progression():
    rand_min = 1
    rand_max = 10
    rand_start = randint(rand_min, rand_max)
    rand_step = randint(rand_min, rand_max)
    progression = list(range(rand_start,
                             rand_start + rand_step * PROGRESSION_SIZE,
                             rand_step))
    censored_progression, correct_el = censor_progression(progression)
    line = " ".join(list(map(str, censored_progression))).replace("None", "..")
    return line, correct_el


def get_question_and_answer():
    return make_progression()
