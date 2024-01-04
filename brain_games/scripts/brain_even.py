from brain_games.scripts.game_utils import (get_name,
                                            get_answer, is_answer_correct)

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
    print(f"Hello, {name}!")
    if is_win_even_game():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
