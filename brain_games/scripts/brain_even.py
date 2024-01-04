from brain_games.scripts.game_utils import get_name, greet_user, \
    get_answer, is_answer_correct, print_end_message

from random import randint


def even_game_step() -> bool:
    start_number = 1
    end_number = 100
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    question = randint(start_number, end_number)
    print(f"Question: {question}")
    correct_answer = "no" if question % 2 else "yes"
    user_answer = get_answer()
    return is_answer_correct(user_answer, correct_answer)


def is_win_even_game() -> bool:
    try_number = 3
    for _ in range(try_number):
        result = even_game_step()
        if result:
            continue
        else:
            return False
    return True


def main():
    print("Welcome to the Brain Games!")
    name = get_name()
    greet_user(name)
    print_end_message(is_win_even_game(), name)


if __name__ == "__main__":
    main()
