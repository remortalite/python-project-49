from brain_games.scripts.game_utils import get_answer, is_answer_correct, \
    get_name, greet_user, print_end_message

from random import randint


def is_prime(number: int) -> bool:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def run_game() -> bool:
    try_number = 3
    for _ in range(try_number):
        print("Answer \"yes\" if given number is prime. "
              "Otherwise answer \"no\".")

        rand_min = 2
        rand_max = 100
        random_number = randint(rand_min, rand_max)
        print("Question:", random_number)

        user_answer = get_answer()
        result = is_answer_correct(user_answer,
                                   "yes" if is_prime(random_number) else "no")
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
