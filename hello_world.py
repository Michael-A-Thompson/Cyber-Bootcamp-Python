#!/usr/bin/python3

from termcolor import colored

print(colored("Hello WOrld", 'red'))

value = input ("WHat is your name? ")

print(colored("My name is ", 'green'),  colored(value, 'yellow'),  colored(" I will be a Python Master", 'blue'))
