#!/usr/bin/env python3
import prompt
from random import randint
import math


def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')


def rules():
    print('Find the greatest common divisor of given numbers.')


def gcd_game():
    count = 0
    while count <= 3:
        num1 = randint(1,30)
        num2 = randint(1,30)
        print('Question: ', num1 , num2)
        answer = prompt.string('Your answer: ' )
        result = math.gcd(num1, num2)
        if answer == str(result):
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
    gcd_game()


if __name__ == '__main__':
    main()
