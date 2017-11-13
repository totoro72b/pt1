from weakref import WeakKeyDictionary

# "the descriptor protocol defines how attribute access is interpreted in the language"

class ExamNoDescriptor(object):
    """A simple class to illustrate the annoyances of repeated property usage"""

    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    def _check_grade(self, value):
        if value < 0 or value > 100:
            raise ValueError("a grade must be between 0 and 100")

    @property
    def math_grade(self):
        return self._math_grade

    @property
    def writing_grade(self):
        return self._writing_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = value

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

##### failed attempt to use descriptors to resolve the issue
class GradeBad(object):
    """Grade descriptor class. bad implementation"""
    def __init__(self):
        self._value = 0

    def __get__(self, instance, instance_type):
        print('instance is {}, type is {}'.format(instance, instance_type))
        return self._value

    def __set__(self, instance, value):
        print('instance is {}, val is {}'.format(instance, value))
        if not (0 <= value <= 100):
            raise ValueError('grade must be between 0 and 100!')
        self._value = value


class Exam(object):
    # class variables
    math_grade = GradeBad()
    writing_grade = GradeBad()


class ExamFailToFix(object):
    """attempt to fix the issues with class variables by using instance vars,
    but does NOT work
    """

    def __init__(self):
        self.math_grade = GradeBad()
        self.writing_grade = GradeBad()

#### fixed version

class GradeFixed(object):
    """GradeFixed descriptor class.
    fix the class variables issue by keeping references of the Exam instances
    """
    def __init__(self):
        self._values = WeakKeyDictionary()  # to prevent memory leak

    def __get__(self, instance, instance_type):
        print('instance is {}, type is {}'.format(instance, instance_type))
        if instance is None:
            return self

        return self._values.get(instance, 0)  # maybe never been set before

    def __set__(self, instance, value):
        print('instance is {}, val is {}'.format(instance, value))
        if not (0 <= value <= 100):
            raise ValueError('grade must be between 0 and 100!')
        self._values[instance] = value


class ExamFixed(object):
    # still class variables, but use fixed version of Grade
    math_grade = GradeFixed()
    writing_grade = GradeFixed()
