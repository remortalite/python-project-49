from random import randint


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_SIZE = 10


def get_progression(size: int) -> list[int]:
    rand_min = 0
    rand_max = 20
    start_number = randint(rand_min, rand_max)
    interval = randint(rand_min, rand_max)

    progression = []
    temp = start_number
    for i in range(size):
        progression.append(temp + i * interval)

    return progression


def censor_progression(progression: list[int]) -> (list[int], int):
    rand_idx = randint(0, len(progression) - 1)
    correct_el = progression[rand_idx]
    progression[rand_idx] = None
    return progression, correct_el


def get_str_progression(progression: list[int]) -> str:
    line = ""
    for el in progression:
        if el:
            line += str(el) + " "
        else:
            line += ".. "
    return line.strip()


def make_progression() -> (str, int):
    progression = get_progression(PROGRESSION_SIZE)
    censored_progression, correct_el = censor_progression(progression)
    return get_str_progression(censored_progression), correct_el


def get_question_and_answer() -> (str, int):
    return make_progression()