import prompt
from random import randint


def even_game_step() -> bool:
    start_number = 1
    end_number = 100
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    question_number = randint(start_number, end_number)
    print(f"Question: {question_number}")
    correct_answer = "no" if question_number % 2 else "yes"
    answer = prompt.string("Your answer:  ")
    if answer.strip() != correct_answer:
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_answer}'.")
        return False
    print("Correct!")
    return True


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
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    if is_win_even_game():
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()
