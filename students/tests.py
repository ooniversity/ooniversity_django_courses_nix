from django.test import TestCase
from .models import Student
from courses.models import Course
from .views import StudentDetailView
from django.test import Client
from lxml import etree


# Create your tests here.
class StudentsListTest(TestCase):

    def test_page_200(self):
        from django.test import Client
        client = Client()

        student = Student.objects.create(
            name='Test_student',
            surname='studentovich',
            date_of_birth='1999-01-01',
            email='em@em.com',
            phone='99393123212',
            address='address',
            skype='skype')

        response = client.get('/students/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Test_student')

    def test_page_by_course(self):
        from django.test import Client
        client = Client()

        Student.objects.create(
            name='not visible',
            surname='not visible',
            date_of_birth='1999-01-01',
            email='em@em.com',
            phone='99393123212',
            address='address',
            skype='skype')

        student = Student.objects.create(
            name='visible_student',
            surname='test',
            date_of_birth='1999-01-01',
            email='em@em.com',
            phone='99393123212',
            address='address',
            skype='skype')

        course = Course.objects.create(
            name='Course_test',
            short_description='Test course creation')
        student.courses = [course]
        student.save()

        qs = Student.objects.filter(courses__id=course.id)
        #print('-----------------------------------')
        #print(qs[0].name)
        #print(qs[0].surname)
        #print(qs[0].courses.all()[0].id)
        #print(qs)

        response = client.get('/students/?course_id=1')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'visible_student')
        self.assertNotContains(response, 'not visible')

    def test_page_paginator_empty(self):
        from django.test import Client
        client = Client()

        response = client.get('/students/')

        self.assertEquals(response.status_code, 200)
        self.assertNotContains(response, '<ul class="pagination">')

    def test_page_pagination_exists(self):
        from django.test import Client
        client = Client()
        for i in range(0, 3):
            Student.objects.create(
                name='name' + str(i),
                surname='not visible',
                date_of_birth='1999-01-01',
                email='em@em.com',
                phone='99393123212',
                address='address',
                skype='skype')

        response = client.get('/students/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, '<ul class="pagination">')

    def test_page_2_per_page(self):
        from django.test import Client
        client = Client()

        for i in range(0, 3):
            Student.objects.create(
                name='name' + str(i),
                surname='not visible',
                date_of_birth='1999-01-01',
                email='em@em.com',
                phone='99393123212',
                address='address',
                skype='skype')

        response = client.get('/students/')

        tree = etree.HTML(response.content)
        r = tree.xpath('//table[@class="table"]/tr')
        #for i in r:
        #    print(i)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(r), 3)

    def test_page_empty(self):
        client = Client()

        response = client.get('/students/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'No students are available.')

    def test_page_context(self):
        client = Client()

        Student.objects.create(
            name='Test_student',
            surname='studentovich',
            date_of_birth='1999-01-01',
            email='em@em.com',
            phone='99393123212',
            address='address',
            skype='skype')

        students = Student.objects.all()

        response = client.get('/students/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(list(response.context['object_list']), list(students))

    def test_page_template(self):
        client = Client()

        response = client.get('/students/')

        self.assertEquals(len(response.templates), 2)
        self.assertEquals(response.templates[0].name, 'students/student_list.html')
        self.assertEquals(response.templates[1].name, 'base.html')

    def test_active_link(self):
        client = Client()

        response = client.get('/students/')
        self.assertContains(response, '<li class="active"><a  href="/students/" >Students</a></li>')


class StudentsDetailTest(TestCase):

    def setUp(self):
        course = Course.objects.create(
                name='Course_test',
                short_description='Test course creation')

        self.student = Student.objects.create(
                name='Test_student',
                surname='studentovich',
                date_of_birth='1999-01-01',
                email='em@em.com',
                phone='99393123212',
                address='address',
                skype='skype')

        self.assertEquals(Student.objects.all().count(), 1)

    def test_page_200(self):
        client = Client()

        response = client.get('/students/1/')

        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'Test_student')

    def test_page_404(self):
        client = Client()

        response = client.get('/students/1000/')

        self.assertEquals(response.status_code, 404)

    def test_page_context(self):
        client = Client()

        response = client.get('/students/1/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.context['student'], self.student)

    def test_page_titles(self):
        client = Client()

        response = client.get('/students/1/')

        self.assertContains(response, '<title>Students detail</title>')

    def test_page_template(self):
        client = Client()

        response = client.get('/students/1/')

        self.assertEquals(len(response.templates), 2)

        self.assertEquals(response.templates[0].name, 'students/student_detail.html')
        self.assertEquals(response.templates[1].name, 'base.html')

    def test_view(self):
        client = Client()

        response = client.get('/students/1/')

        self.assertEquals(response.resolver_match.func.__name__, StudentDetailView.as_view().__name__)
