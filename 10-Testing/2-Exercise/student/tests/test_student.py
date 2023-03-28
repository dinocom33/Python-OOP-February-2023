from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):

    def setUp(self) -> None:
        self.student = Student("name")
        self.student_with_course = Student("name1", {"python": []})

    def test_correct_initialization(self):
        self.assertEqual(self.student.name, "name")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(self.student_with_course.name, "name1")
        self.assertEqual(self.student_with_course.courses, {"python": []})

    def test_add_notes_in_existing_course(self):
        result = self.student_with_course.enroll("python", ["first note"])
        self.assertEqual(self.student_with_course.courses["python"][0], "first note")
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_add_course_and_notes_without_add_course_notes(self):
        result = self.student.enroll("python", ["first note"])
        self.assertEqual(self.student.courses["python"][0], "first note")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_course_and_notes_with_add_course_notes_y(self):
        result = self.student.enroll("python", ["first note"], "Y")
        self.assertEqual(self.student.courses["python"][0], "first note")
        self.assertEqual(result, "Course and course notes have been added.")

    def test_add_new_course_without_notes(self):
        result = self.student.enroll("python", ["notes"], "N")
        self.assertEqual(self.student.courses, {"python": []})
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_to_existing_course(self):
        result = self.student_with_course.add_notes("python", "first note")
        self.assertEqual(self.student_with_course.courses["python"][0], "first note")
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("python", "first note")

        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_existing_course(self):
        result = self.student_with_course.leave_course("python")
        self.assertEqual(self.student_with_course.courses, {})
        self.assertEqual(result, "Course has been removed")

    def test_leave_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("python")

        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")


if __name__ == '__main__':
    main()
