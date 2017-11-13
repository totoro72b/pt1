import unittest

from item_31_use_descriptors_for_resuable_property import (ExamNoDescriptor,
                                                           Exam,
                                                           ExamFailToFix,
                                                           ExamFixed,
                                                           GradeBad)


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
        """Test that BadGrade breaks as expected"""

        exam1 = Exam()
        exam2 = Exam()

        exam1.math_grade = 10

        self.assertEqual(exam1.math_grade, 10)

        self.assertEqual(exam2.math_grade, 10)  # bad! because of instance variables, exam2 value also got changed


    def test_fail_to_fix(self):
        """use GradeBad as instance variables does NOT solve the problem"""

        exam1 = ExamFailToFix()
        exam2 = ExamFailToFix()

        exam1.math_grade = 10

        self.assertEqual(exam1.math_grade, 10)
        self.assertEqual(type(exam1.writing_grade), GradeBad)  # bad! the unassigned value is an instance of BadGrade!

    def test_fixed_grades(self):
        """Test that FixedGrade works as expected"""

        exam1 = ExamFixed()
        exam2 = ExamFixed()

        exam1.math_grade = 10

        self.assertEqual(exam1.math_grade, 10)
        self.assertEqual(exam2.math_grade, 0)
