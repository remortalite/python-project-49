from random import randint


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_SIZE = 10


def censor_progression(progression: list[int]) -> (list[int], int):
    rand_idx = randint(0, len(progression) - 1)
    correct_el = progression[rand_idx]
    progression[rand_idx] = None
    return progression, correct_el


def get_str_progression(progression: list[int]) -> str:
    line = ""
    for el in progression:
        if el is not None:
            line += str(el) + " "
        else:
            line += ".. "
    return line.strip()


def make_progression() -> (str, int):
    rand_min = 1
    rand_max = 10
    rand_start = randint(rand_min, rand_max)
    rand_step = randint(rand_min, rand_max)
    progression = list(range(rand_start,
                             rand_start + rand_step * PROGRESSION_SIZE,
                             rand_step))
    censored_progression, correct_el = censor_progression(progression)
    return get_str_progression(censored_progression), correct_el


def get_question_and_answer() -> (str, int):
    return make_progression()
