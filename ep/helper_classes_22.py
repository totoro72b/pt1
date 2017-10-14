from collections import namedtuple

# item 22: use helper classes -- Oct 7
class GradeBook(object):
    """GradeBook class
    keep track of students and their grades
    """
    def __init__(self):
        self.students = {}

    def report_grade(self, student, subject, score_data):
        """Report the grade for a student for a subject, score and weight"""
        student = self.students.setdefault(student, Student())
        student.report_grade(subject, **score_data)

    def get_average_grade(self, student, subject):
        """Report the grade for a student for a subject, score and weight"""
        student = self.students[student]
        return student.get_average_grade(subject)


class Student(object):
    """Student Class. keep track of subjects for each student"""
    def __init__(self):
        self.grades = {}

    def report_grade(self, subject, **kwargs):  # inconsitency for now...
        """Report a grade for a subject with given score and weight"""
        score = kwargs.pop('score')
        weight = kwargs.pop('weight')
        if kwargs:
            raise ValueError('Unexpected kwargs {}'.format(kwargs))
        subject = self.grades.setdefault(subject, Subject())
        subject.report_grade(score, weight)

    def get_average_grade(self, subject):
        """Get the average grade given a subject"""
        return self.grades[subject].get_average_grade()


Grade = namedtuple('Grade', ['score', 'weight'])


class Subject(object):
    """Subject class. keep track of the weighted grades for a given subject"""

    # grades = []  # a list of namedtuple
    def __init__(self):
        super(Subject, self).__init__()
        self.grades = []

    def get_average_grade(self):
        """Return the wieghted average of all the grades"""
        total_score = 0.0
        total_weight = 0.0
        for g in self.grades:
            total_score += g.score * g.weight
            total_weight += g.weight

        return total_score / total_weight

    def report_grade(self, score, weight):
        """record a given grade and its weight"""
        g = Grade(score=score, weight=weight)
        self.grades.append(g)

