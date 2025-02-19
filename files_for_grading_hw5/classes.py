from funcs import add_comment

class problem:
    def __init__(self, module):
        self.module = module
        self.n = 0
        self.prob_grade, self.prob_comment = 0, ''

    def add_prob_grade_and_comment(self, func):
        grade, comment = func()
        self.prob_grade += grade
        self.prob_comment = add_comment(self.prob_comment, comment)

    def normalize_grade(self):
        self.prob_grade /= self.n
