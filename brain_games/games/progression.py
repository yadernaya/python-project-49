from random import randint
import math
import prompt

name = ''

def greet():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def rules():
    print('What number is missing in the progression?')


def progression_game():
    count = 0
    while count <= 3:
        step = randint(1,6)
        start = randint(0,10)
        progr_length = randint(5, 9)
        end = start + progr_length*step
        index = progr_length - 1
        progressive = []
        for symbol in range(start, end, step):
            progressive.append(symbol)
        x_number = progressive[index]
        progressive[index] = '..'
        print('Question: ', *progressive)
        answer = prompt.string('Your answer: ' )
        if answer == str(x_number):
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was\'{x_number}\'\nLet\'s try again, {name}!')
            break


