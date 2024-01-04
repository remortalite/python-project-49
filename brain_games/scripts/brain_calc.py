from brain_games.scripts.game_utils import get_name, greet_user, \
    get_answer, is_answer_correct, print_end_message

from random import randint, choice


def get_random_expression() -> (str, int):
    """ Returns: (expression, result) """
    start_number = 0
    end_number = 100
    random_operation = choice(["+", "-", "*"])
    random_number_1 = randint(start_number, end_number)
    random_number_2 = randint(start_number, end_number)
    result = "?"
    match random_operation:
        case "+":
            result = random_number_1 + random_number_2
        case "-":
            result = random_number_1 - random_number_2
        case "*":
            result = random_number_1 * random_number_2
    return (f"{random_number_1} {random_operation} {random_number_2}",
            str(result))


def run_game() -> bool:
    try_number = 3
    for _ in range(try_number):
        expr, correct_answer = get_random_expression()

        print("What is the result of the expression?")
        print("Question: ", expr)

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
