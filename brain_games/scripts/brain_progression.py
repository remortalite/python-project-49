from brain_games.scripts.game_utils import get_answer, is_answer_correct, \
    get_name, greet_user, print_end_message

from random import randint


def get_progression(size: int) -> list[int]:
    rand_min = 0
    rand_max = 100
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


def make_progression(size: int) -> (str, int):
    progression = get_progression(size)
    censored_progression, correct_el = censor_progression(progression)
    return get_str_progression(censored_progression), correct_el


def run_game() -> bool:
    try_number = 3
    for _ in range(try_number):
        print("What number is missing in the progression?")

        size = 10
        progression, correct_answer = make_progression(size)
        print("Question:", progression)

        user_answer = get_answer()
        result = is_answer_correct(user_answer, correct_answer)
        if result:
            continue
        else:
            return False
    return True


def main():
    name = get_name()
    greet_user(name)

    result = run_game()
    print_end_message(result, name)


if __name__ == "__main__":
    main()
