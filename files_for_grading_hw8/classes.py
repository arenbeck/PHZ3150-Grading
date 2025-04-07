from funcs import add_comment, return_att
import numpy as np

# Problem class for each problem in the notebook (or part of a problem)
# Contains functions that should make grading easier
class problem:
    def __init__(self, module):
        self.module = module
        self.n = 0
        self.prob_grade, self.prob_comment = 0, ''

    # Adds the grade and comment from a grading function to the total grade and "total" comment
    def add_prob_grade_and_comment(self, func):
        grade, comment = func
        self.prob_grade += grade
        self.prob_comment = add_comment(self.prob_comment, comment)

    # Normalizes the problem grade depending on the number of grading functions
    def normalize_grade(self):
        self.prob_grade /= self.n

    # Grades a set of variables
    # var_list is a list with the name of the variables
    # values is a list with the value that each variable in var_list should have
    def grade_variables(self, var_list, values):
        # Helper function that grades a single variable
        def grade_single_variable(var_name, var_value):
            var = return_att(self.module, var_name)
            if type(var) == None:
                return 0, f'No variable named {var_name}.'

            if type(var_value) != type(var):
                return 0.25, f'Variable {var_name} is not the correct type.'

            if type(var_value) == type(np.array([])):
                if not np.array_equal(var, var_value):
                    return 0.5, f'Variable {var_name} is not correct.'
            else:
                if var != var_value:
                    return 0.5, f'Variable {var_name} is not correct.'

            return 1, ''

        # Helper function that grades multiple variables
        def grade_multiple_variables(var_names, var_values):
            grade, comment = 0, ''
            for v_name, v_val in zip(var_names, var_values):
                g, c = grade_single_variable(v_name, v_val)
                grade += g
                comment = add_comment(comment, c)

            return grade/len(var_names), comment

        return grade_multiple_variables(var_list, values)

    # Grades multiple functions in the notebook
    # func_names is a list of function names that need to be graded
    # sol_funcs is a list of functions (not the name, the actual function) that give the correct output to the graded functions
    # inputs is a list with the necessary inputs for each function (may be a list of lists).
    def grade_functions(self, func_names, sol_funcs, inputs):
        # Helper function to check the output of each function, not perfect, needs some work
        def check_output(output, solution):
            if type(output) != type(solution):
                return False

            if type(solution) == type(np.array([])):
                if not np.allclose(output, solution, rtol=0.01):
                    return False
            else:
                if not np.allclose(output, solution, rtol=0.01):
                    return False

            return True

        # Helper function that grades a single function
        def grade_single_function(func_name, sol_func, input):
            func = return_att(self.module, func_name)
            if func == None:
                return 0, f'No function named {func_name}.'

            try:
                output = func(*input)
                sol_output = sol_func(*input)
                if not check_output(output, sol_output):
                    return 0.5, f'The function {func_name} did not return the right output.'
            except Exception as e:
                print(e)
                return 0, f'The function {func_name} did not take the right input or did not return the output in the right format.'

            return 1, ''

        # Helper function that grades multiple functions
        def grade_multiple_functions(func_names, sol_funcs, inputs):
            grade, comment = 0, ''
            for f_name, sol_f, input in zip(func_names, sol_funcs, inputs):
                g, c = grade_single_function(f_name, sol_f, input)
                grade += g
                comment = add_comment(comment, c)

            return grade/len(func_names), comment

        return grade_multiple_functions(func_names, sol_funcs, inputs)
