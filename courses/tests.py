from django.test import TestCase
from .models import Course
from django.test import Client
from .views import CourseDetailView


# Create your tests here.
class CoursesListTest(TestCase):

    def test_page_200(self):
        client = Client()

        self.course = Course.objects.create(
            name='Course_test',
            short_description='Test course creation')
        self.assertEquals(Course.objects.all().count(), 1)

        response = client.get('/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Course_test'.upper())

    def test_page_empty(self):
        client = Client()

        response = client.get('/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'No courses are available.')

    def test_page_context(self):
        client = Client()

        Course.objects.create(
            name='Course_test',
            short_description='Test course creation')

        courses = Course.objects.all()

        response = client.get('/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(list(response.context['courses_list']), list(courses))

    def test_page_template(self):
        client = Client()

        response = client.get('/')

        self.assertEquals(len(response.templates), 2)
        self.assertEquals(response.templates[0].name, 'index.html')
        self.assertEquals(response.templates[1].name, 'base.html')

    def test_active_link(self):
        client = Client()

        response = client.get('/')
        self.assertContains(response, '<li class="active"><a href="/">Main</a></li>')


class CoursesDetailTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name='Course_test',
            short_description='Test course creation')
        self.assertEquals(Course.objects.all().count(), 1)

    def test_page_200(self):
        client = Client()

        response = client.get('/courses/1/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Course_test')

    def test_page_404(self):
        client = Client()

        response = client.get('/courses/1000/')

        self.assertEquals(response.status_code, 404)

    def test_page_context(self):
        client = Client()

        response = client.get('/courses/1/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['course_obj'], self.course)

    def test_page_titles(self):
        client = Client()

        response = client.get('/courses/1/')

        self.assertContains(response, '<h3>Teachers</h3>')
        self.assertContains(response, '<h2>Lessons plan</h2>')

    def test_page_template(self):
        client = Client()

        response = client.get('/courses/1/')

        self.assertEquals(len(response.templates), 2)

        self.assertEquals(response.templates[0].name, 'courses/detail.html')
        self.assertEquals(response.templates[1].name, 'base.html')

    def test_view(self):
        client = Client()

        response = client.get('/courses/1/')

        self.assertEquals(response.resolver_match.func.__name__, CourseDetailView.as_view().__name__)

    def test_active_link(self):
        client = Client()

        response = client.get('/courses/1/')

        self.assertContains(response, '<li class="active"><a href="/">Main</a></li>')