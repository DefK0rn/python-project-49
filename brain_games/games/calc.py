import random

import prompt

from brain_games.engine import right_answer, wrong_answer

MAX_STEP = 3
SUPPORTED_OPERATIONS = ['+', '-', '*']


def get_result(number1, operation, number2):
    match operation:
        case '+':
            return number1 + number2
        case '-':
            return abs(number1 - number2)
        case '*':
            return number1 * number2


def check_calc(name):
    print('What is the result of the expression?')
    step = 1

    while step <= MAX_STEP:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        operation = random.choice(SUPPORTED_OPERATIONS)

        print(f"Question: {number1 if number1 > number2 else number2}", end=" ")
        print(f"{operation} {number2 if number1 > number2 else number1}")
        answer = prompt.integer('Your answer: ')
        correct_answer = get_result(number1, operation, number2)

        if answer != correct_answer:
            return wrong_answer(name, answer, correct_answer)
        else:
            print('Correct!')

        step += 1

    right_answer(name)