from random import randint, choice


DESCRIPTION = "What is the result of the expression?"


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


def get_question_and_answer() -> (str, int):
    return get_random_expression()