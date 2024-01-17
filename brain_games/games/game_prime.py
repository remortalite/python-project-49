from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_question_and_answer() -> (str, str):
    rand_min = 2
    rand_max = 100
    random_number = randint(rand_min, rand_max)
    return str(random_number), "yes" if is_prime(random_number) else "no"
