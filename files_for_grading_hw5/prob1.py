from funcs import return_att, same_list
import numpy as np
import matplotlib.pyplot as plt
from classes import problem


class prob1(problem):
    def __init__(self, module):
        super().__init__(module)

        self.add_prob_grade_and_comment(self.check_variables)


    def check_variables(self):
        
        grade = 0
        comment = ""
        #Not checking if numpy and matplot lib are imported for now:
        grade+=2
        
        #Check that x, y, z arrays exist and are correct:
        
        var_names = ['x','y','z']
        for var in var_names:
            values = return_att(self.module, var)
            if values is not None: #variable exists (not checking that it is a list) get the values.
                grade += 2
                if var =='x':
                    xx = values
                    n_elements = len(values)
                    if n_elements != 100: #100 elements?
                        comment += f'x does not contain the correct number of elements.\n'
                        grade -= 1
                    if (values[1] - values[0]) !=0.5: #step size = 0.5?
                        comment += f'x does not have the correct step size.\n'
                        grade -= 1
                elif var == 'y': 
                    if len(np.where(values == np.log10(xx))[0]) != 0:
                        comment += f'y values are not log_10 of x values.\n'
                        grade -= 2
                else: #var == z
                    if len(np.where(values == np.sqrt(xx))[0]) != 0:
                        comment += f'y values are not square roots of x values.\n'
                        grade -= 2
            else: #no variable assigned with that name.
                grade -=2
                comment += f'no variable named {var} assigned.\n'
                
        #Not checking if figure is produced for now:            
        #try:
        #    subprocess.run(command, check=True, timeout=5)            
        #    return bool(plt.get_fignums())  # Returns True if a figure is open
        #except Exception:
        #    return False 
        grade +=4

        #Not checking for .pdf for now:
        grade +=2

        #Not checking for comments in code for now:

        grade +=1

        return grade, comment


