from funcs import return_att, same_list
import numpy as np
from classes import problem
import random
import string


def inputs():
    def generate_random_word(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def create_random_word_list(num_words, min_length, max_length):
        return [generate_random_word(random.randint(min_length, max_length)) for _ in range(num_words)]

    num_words = 20
    min_length = 1
    max_length = 100
    random_word_list = create_random_word_list(num_words, min_length, max_length)
    return random_word_list



def func_sol(list_of_words):
    largest_word = ''
    for word in list_of_words:
        if len(word) > len(largest_word):
            largest_word = word
    return largest_word


class prob1(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variables)
        self.add_prob_grade_and_comment(self.check_for_loop_function)
        self.add_prob_grade_and_comment(self.check_while_loop_function)

        self.n = 3
        self.normalize_grade()

    def check_variables(self):
        var_sol = "Deleting an item from a list or array while iterating over it is a Python problem that is well known to any experienced software developer".split()

        list_of_words = return_att(self.module, 'list_of_words')
        if list_of_words == None:
            return 0, 'No variable named "list_of_words".'

        if var_sol != list_of_words:
            return 0.5, 'Variable "list_of_words" does not have the correct value.'

        return 1, ''

    def check_for_loop_function(self):
        function_name = 'largest_word_for_loop'
        func = return_att(self.module, function_name)
        if func == None:
            return 0, f'No function named {function_name}.'

        inp = inputs()

        try:
            result = func_sol(inp) == func(inp)
            if not result:
                return 0.5, f'The function {function_name} did not return the right output.'

            return 1, ''
        except Exception as e:
            return 0, f'The function did not take the right input. Error: {str(e)}'

    def check_while_loop_function(self):
        function_name = 'largest_word_while_loop'
        func = return_att(self.module, function_name)
        if func == None:
            return 0, f'No function named {function_name}.'

        inp = inputs()

        try:
            result = func_sol(inp) == func(inp)
            if not result:
                return 0.5, f'The function {function_name} did not return the right output.'

            return 1, ''
        except Exception as e:
            return 0, f'The function did not take the right input. Error: {str(e)}'
