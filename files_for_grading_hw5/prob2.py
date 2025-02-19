from funcs import return_att, same_list
import numpy as np
from classes import problem

class prob2(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variable)

    def check_variable(self):
        grade = 10
        comment = ""

        #checks for q: 
        
        qq = return_att(self.module, 'q')
        if qq is not None: # q exists 
            if type(qq) != type(np.array([])):
                comment += 'q is not a numpy array.\n'
                grade -= 0.5

        else:
            grade -= 1
            comment += 'no variable named q.\n'

        #not checking for print statements for now: (2 points)

        #checks for q_list:
        
        ql = return_att(self.module,'q_list')
        
        if ql is not None: #q_list exists
                if type(ql) != type([]):
                    comment += 'q_list is not a list.\n'
                    grade -= 1

                #not checking for printed statements: (1 point)

                if ql[28] != 42:
                    comment += 'q_list[28] was not changed to 42.'
                    grade -= 1

                #not checking for explanation: (0.5 point)

        else:
            grade -= 1
            comment += 'no variable named q_list.\n'

                #checks for q_list:
        
        qt = return_att(self.module,'q_tuple')
        
        if qt is not None: #q_tuple exists
                if type(qt) != type(()): #is tuple?
                    comment += 'q_list is not a tuple.'
                    grade -= 1

                #not checking for printed statements: (1 point)

                if ql[28] != 42:
                    comment += 'q_list[28] was not changed to 42.'
                    grade -= 1

                #not checking for print statements: (1 point)
                #not checking for tuple assignment error: (1 point)
                #not checking for explanation: (0.5 point)

        else:
            grade -= 1
            comment += 'no variable named q_tuple.\n'


        return grade, comment