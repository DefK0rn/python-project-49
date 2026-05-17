import math
import random

import prompt

from brain_games.engine import right_answer, wrong_answer

MAX_STEP = 3


def get_result(number1, number2):
    return math.gcd(number1, number2)


def check_gcd(name):
    print('Find the greatest common divisor of given numbers.?')
    step = 1

    while step <= MAX_STEP:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)

        print(f"Question: {number1} {number2}")
        answer = prompt.integer('Your answer: ')
        correct_answer = get_result(number1, number2)

        if answer != correct_answer:
            return wrong_answer(name, answer, correct_answer)
        else:
            print('Correct!')

        step += 1

    right_answer(name)