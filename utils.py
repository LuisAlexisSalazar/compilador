from termcolor import colored
import os


def error(message):
    print(colored(message, 'red'))


def existFile(path):
    return os.path.exists(path)
