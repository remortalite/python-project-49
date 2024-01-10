from brain_games.scripts.game_utils import get_name, greet_user, \
    get_answer, is_answer_correct, print_end_message

from random import randint


def find_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    a, b = sorted([a, b], reverse=True)
    a -= (a // b) * b
    return find_gcd(*sorted([a, b], reverse=True))


def gcd_game_step() -> bool:
    start_number = 1
    end_number = 100
    print("Find the greatest common divisor of given numbers.")
    question: (int, int) = (randint(start_number, end_number),
                            randint(start_number, end_number))
    print(f"Question: {question[0]} {question[1]}")
    correct_answer = find_gcd(*question)
    user_answer = get_answer()
    return is_answer_correct(user_answer, correct_answer)


def is_win_game() -> bool:
    try_number = 3
    for _ in range(try_number):
        result = gcd_game_step()
        if result:
            continue
        else:
            return False
    return True


def main():
    print("Welcome to the Brain Games!")
    name = get_name()
    greet_user(name)
    print_end_message(is_win_game(), name)


if __name__ == "__main__":
    main()
