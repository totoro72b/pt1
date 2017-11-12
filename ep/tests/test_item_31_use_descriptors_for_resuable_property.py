import unittest

from item_31_use_descriptors_for_resuable_property import (ExamNoDescriptor,
                                                           Exam)


class TestDescriptors(unittest.TestCase):
    """Test the usage of descriptors"""

    def test_no_descriptors(self):
        """Test the dumb examples work"""
        exam = ExamNoDescriptor()
        exam.math_grade = 90
        exam.english_grade = 70

        self.assertEqual(exam.math_grade, 90)
        self.assertEqual(exam.english_grade, 70)

        with self.assertRaises(ValueError):
            exam.math_grade = -1

        with self.assertRaises(ValueError):
            exam.writing_grade = 101


    def test_bad_grades(self):
        """Test that bad grades break as expected"""

        exam1 = Exam()
        exam2 = Exam()

        exam1.math_grade = 10

        self.assertEqual(exam1.math_grade, 10)

        with self.assertRaises(AssertionError):
            assert exam2.math_grade == 0  # breaks because of instance variables
