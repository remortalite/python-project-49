from random import randint


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_SIZE = 10


def make_progression():
    rand_min = 1
    rand_max = 10
    rand_start = randint(rand_min, rand_max)
    rand_step = randint(rand_min, rand_max)
    progression = list(range(rand_start,
                             rand_start + rand_step * PROGRESSION_SIZE,
                             rand_step))

    rand_idx = randint(0, len(progression) - 1)
    correct_el = progression[rand_idx]
    progression[rand_idx] = ".."
    line = " ".join(list(map(str, progression)))
    return line, correct_el


def get_question_and_answer():
    return make_progression()
