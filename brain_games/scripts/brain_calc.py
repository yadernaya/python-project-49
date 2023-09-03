#!/usr/bin/env python3

import prompt
from random import randint
from random import choice
import operator

def greet():
    print('Welcome to the Brain Games!')


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    return (f'Hello, {name}!')


def rules_of_game():
    print('What is the result of the expression?')


def calc_game():
    attempts = 3
    count = 0
    operators = ('+', '-', '*')
    while count <= attempts:
      num1 = randint(20, 40)
      num2 = randint(1, 20)
      random_oper = choice(operators)
      print('Question: ', num1, random_oper , num2)
      count += 1
      if random_oper == '+':
        result = operator.add(num1, num2)
      if random_oper == '-':
        result = operator.sub(num1, num2)
      if random_oper == '*':
        result = operator.mul(num1, num2)
      answer = prompt.string('Your answer: ')
      if answer == str(result):
        print('Correct!')
        if count == 3:
          print('Congratulations, ', name, '!')
          break
      else:
        print(f'"{answer}" is wrong answer ;(. Correct answer was {result}.\nLet\'s try again, {name}!')
        break


def main():
    greet()
    print(welcome_user())
    rules_of_game()
    calc_game()


if __name__ == '__main__':
    main()
