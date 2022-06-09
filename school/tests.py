from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Assignment
from .forms import CourseForm, AssignmentForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class CourseTest(TestCase):
    def setUp(self):
        self.course=Course(courseTitle='English 101', instructor='Dr.Don', courseTime='12:00', roomNumber=1102, description='Entry level writing')

    def test_string(self):
        self.assertEqual(str(self.course), 'English 101')

    def test_tablename(self):
        self.assertEqual(str(Course._meta.db_table), 'course')

class AssignmentTest(TestCase):
    def setUp(self):
        self.assignment=Assignment(assignmentName='autobiography', dueDate='1/1/2022', assignmentDetails='Write about yourself')

    def test_string(self):
        self.assertEqual(str(self.assignment), 'autobiography')

    def test_tablename(self):
        self.assertEqual(str(Assignment._meta.db_table), 'assignment')