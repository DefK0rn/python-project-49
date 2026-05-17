import random

import prompt

from brain_games.engine import right_answer, wrong_answer

MAX_STEP = 3


def get_progression():
    current_element = random.randint(1, 20)
    progression_number = random.randint(5, 20)
    elements_count = random.randint(5, 11)

    progression = []
    progression_step = 1
    while progression_step <= elements_count:
        progression.append(str(current_element))
        current_element += progression_number
        progression_step += 1

    question_index = random.randint(0, elements_count - 1)
    correct_answer = progression[question_index]
    progression[question_index] = '..'

    return progression, correct_answer


def check_progression(name):
    print('What number is missing in the progression?')
    step = 1

    while step <= MAX_STEP:
        
        progression, correct_answer = get_progression()
        print(f"Question: {' '.join(progression)}")
        answer = prompt.integer('Your answer: ')

        if str(answer) != correct_answer:
            return wrong_answer(name, answer, correct_answer)
        else:
            print('Correct!')

        step += 1

    right_answer(name)