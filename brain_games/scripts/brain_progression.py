#!/usr/bin/env python3

import prompt
from random import randint
import math


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    return ('Hello, ' + name + '!')


def rules():
    print('What number is missing in the progression?')


def progression_game():
    count = 0
    while count <= 3:
        step = randint(1,6)
        start = randint(0,10)
        end = start + 9*step
        index = randint(1, 8)
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
                print('Congratulations, ', name, '!')
                break
        else:
            print(f'"{answer}" is wrong answer ;(.\nLet\'s try again, {name}')
            break


def main():
    greet()
    print(welcome_user())
    rules()
    progression_game()


if __name__ == '__main__':
    main()