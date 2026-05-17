import math
import random

import prompt

from brain_games.engine import right_answer, wrong_answer

MAX_STEP = 3
ANSWERS = {
    True: 'yes',
    False: 'no'
}


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def check_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    step = 1

    while step <= MAX_STEP:
        number = random.randint(1, 100)

        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        correct_answer = ANSWERS.get(is_prime(number))

        if answer != correct_answer:
            return wrong_answer(name, answer, correct_answer)
        else:
            print('Correct!')

        step += 1

    right_answer(name)