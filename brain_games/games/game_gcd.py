from random import randint


DESCRIPTION = "Find the greatest common divisor of given numbers."

def find_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    a, b = sorted([a, b], reverse=True)
    a -= (a // b) * b
    return find_gcd(*sorted([a, b], reverse=True))


def get_question_and_answer() -> (str, str):
    rand_min = 1
    rand_max = 100
    question: (int, int) = (randint(rand_min, rand_max),
                            randint(rand_min, rand_max))
    question_str: str = f"{question[0]} {question[1]}"
    answer = find_gcd(*question)
    return question_str, str(answer)