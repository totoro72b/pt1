import unittest
from helper_classes_22 import Subject, Student, GradeBook

# tests for item 22 helper classes

class TestGradeBook(unittest.TestCase):
    """Test GradeBook class"""

    def setUp(self):
        self.book = GradeBook()

    def test_gradebook_report_grade_and_get_average_grade(self):
        """Test that we correctly report grades and get averages for students"""
        self.book.report_grade('Jim', 'Math', {'score':50, 'weight':0.3})
        self.book.report_grade('Jim', 'Math', {'score':100, 'weight':0.7})

        self.book.report_grade('Tim', 'Math', {'score':100, 'weight':0.3})
        self.book.report_grade('Tim', 'Math', {'score':100, 'weight':0.7})

        self.book.report_grade('Tim', 'Bio', {'score':20, 'weight':0.3})
        self.book.report_grade('Tim', 'Bio', {'score':100, 'weight':0.7})

        self.assertEqual(self.book.get_average_grade('Jim', 'Math'), 85)
        self.assertEqual(self.book.get_average_grade('Tim', 'Math'), 100)
        self.assertEqual(self.book.get_average_grade('Tim', 'Bio'), 76)

class TestStudent(unittest.TestCase):
    """Test Student class"""
    def setUp(self):
        self.student = Student()

    def test_report_grade_and_get_average_grade(self):
        """Test reporting and getting average is correctly computed for each subject"""
        self.student.report_grade('Math', score=50, weight=0.3)
        self.student.report_grade('Math', score=100, weight=0.7)

        #check math is correct
        self.assertEqual(self.student.get_average_grade('Math'), 85)  # 15+70 = 85

        self.student.report_grade('English', score=60, weight=0.3)
        self.student.report_grade('English', score=40, weight=0.2)
        self.student.report_grade('English', score=80, weight=0.5)

        # assert both subjects are correct
        self.assertEqual(self.student.get_average_grade('English'), 66)  # 18+8+40=66
        self.assertEqual(self.student.get_average_grade('Math'), 85)  # 15+70 = 85



class TestSubject(unittest.TestCase):
    """Test Subject class"""

    def setUp(self):
        self.subject = Subject()

    def test_report_grade_and_get_average_int(self):
        """Test grades are correctly reported and average are correctly computed"""

        # only integers
        self.subject.report_grade(100, 1)
        self.assertEqual(self.subject.get_average_grade(), 100)

        self.subject.report_grade(70, 3)
        self.assertEqual(self.subject.get_average_grade(), 77.5)  # 310/4 = 77.5


    def test_report_grade_and_get_average_float(self):
        """Test grades are correctly reported and average are correctly computed"""

        self.subject.report_grade(90, 0.3)
        self.assertEqual(self.subject.get_average_grade(), 90)

        self.subject.report_grade(60, 0.7)
        self.assertEqual(self.subject.get_average_grade(), 69)  # 42 + 27 = 69
