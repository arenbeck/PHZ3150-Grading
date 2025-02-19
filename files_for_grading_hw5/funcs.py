import importlib.util, os, sys


def import_module(module_name):
    # Open a file in write mode to save the output not to clutter terminal
    with open('output.txt', 'w') as f:
        sys.stdout = f  # Redirect stdout to the file

        spec = importlib.util.spec_from_file_location("module_name", module_name)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        sys.stdout = sys.__stdout__
    return module


def return_att(module, function_name):
    '''Return the grade and the comment to be added'''
    # Check if the variable exists and has the expected value
    if hasattr(module, function_name):
        function = getattr(module, function_name)
        return function
    return None


def print_to_file(grade, comment):
    with open('output.txt', 'w') as f:
        f.write(f'{grade}\n{comment}\n')


def add_comment(final, comment, problem = None):
    if comment != '':
        if problem != None:
            if final != '':
                return final + f'\n{problem}:\n' + comment
            return f'{problem}:\n' + comment
        else:
            if final != '':
                return final + '\n' + comment
            return comment
    return final


def same_list(list1, list2):
    if not all(type(l) == type([]) for l in [list1, list2]): return False

    for i in list1:
        for j in list2:
            if round(i, 5) == round(j, 5): return True
    return False
