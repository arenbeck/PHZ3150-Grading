from funcs import return_att, same_list
import numpy as np
from classes import problem

def inputs():
    wl = "The quick brown fox jumped over the lazy dog"
    wl = wl.split()
    checkwords = "quick dog whale ran fox house red a the"
    checkwords = checkwords.split()
    return checkwords, wl

def func_sol(word, list_of_words):
    if word in list_of_words:
        return True
    return False

class prob3(problem):
    grade = 10
    comment = ""
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variable)
        self.add_prob_grade_and_comment(self.check_function)
        
    def check_variable(self):
        #checks for word_list:
        wl = return_att(self.module, 'word_list')
        if wl is not None: # word_list exists 
            if type(wl) != type([]):
                self.comment += 'word_list is not a list.\n'
                self.grade -= 1
            elif wl != ['twinkle','twinkle','little','star']:
                self.comment += 'word_list does not contain the correct words.\n'
                self.grade -= 1

        # not checking for students to find letters yet: (2 points)
        return

    def check_function(self):
        #not checking for printed statements yet.
        
        func = return_att(self.module, 'word_in_list')
        if func == None:
            self.comment += 'No function named word_in_list.\n'
            self.grade -= 3

        cw, cwl = inputs()

        try:
            gr = 0
            for word in cw:
                a = func_sol(word, cwl)
                b = func(word, cwl)
                if a ^ b: #a XOR b implies that outputs differ.
                    self.comment += "Word_in_list returned incorrect results.\n"
                    gr = 1
            self.grade -= gr
                                                    
        except:
            
            self.comment += "Word_in_list did not run without errors.\n"
            self.grade -= 1

        #not checking for comments yet. (1 point)

        return
            



