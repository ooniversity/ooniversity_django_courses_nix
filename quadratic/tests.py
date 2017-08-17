"""Quadrantic Result Test Case"""

from django.test import SimpleTestCase, RequestFactory
from .views import ResultsView, ERROR_UNDEFINED, ERROR_DIGIT, ERROR_A_ZERO, ERROR_D_NEGATIVE


class ResultsTest(SimpleTestCase):
    """Result View Test Case"""
    def setUp(self):
        """Before Tests"""
        self.request = RequestFactory()
        self.view = ResultsView()

    def test_without_get(self):
        """/quadratic/results/"""
        self.view.request = self.request.get('/quadratic/results/')

        context = self.view.get_context_data()

        self.assertEqual('', context['items']['a'])
        self.assertEqual('', context['items']['b'])
        self.assertEqual('', context['items']['c'])

        self.assertDictEqual({'a': ERROR_UNDEFINED, 'b': ERROR_UNDEFINED, 'c': ERROR_UNDEFINED}, context['errors'])


    def test_without_b_and_invalid_c(self):
        """/quadratic/results/?a=1&b=&c=st"""
        self.view.request = self.request.get('/quadratic/results/?a=1&b=&c=st')

        context = self.view.get_context_data()

        self.assertEqual('1', context['items']['a'])
        self.assertEqual('', context['items']['b'])
        self.assertEqual('st', context['items']['c'])

        self.assertDictEqual({'b': ERROR_UNDEFINED, 'c': ERROR_DIGIT}, context['errors'])


    def test_zero_a_and_zero_c_and_zero_c(self):
        """/quadratic/results/?a=0&b=0&c=0"""
        self.view.request = self.request.get('/quadratic/results/?a=0&b=0&c=0')

        context = self.view.get_context_data()

        self.assertEqual('0', context['items']['a'])
        self.assertEqual('0', context['items']['b'])
        self.assertEqual('0', context['items']['c'])

        self.assertDictEqual({'a': ERROR_A_ZERO}, context['errors'])

    def test_without_a_and_invalid_b_and_negative_c(self):
        """/quadratic/results/?a=&b=ts&c=-4"""
        self.view.request = self.request.get('/quadratic/results/?a=&b=ts&c=-4')

        context = self.view.get_context_data()

        self.assertEqual('', context['items']['a'])
        self.assertEqual('ts', context['items']['b'])
        self.assertEqual('-4', context['items']['c'])

        self.assertDictEqual({'a': ERROR_UNDEFINED, 'b': ERROR_DIGIT}, context['errors'])

    def test_negative_a_and_b_and_c(self):
        """/quadratic/results/?a=-1&b=2&c=35"""
        self.view.request = self.request.get('/quadratic/results/?a=-1&b=2&c=35')

        context = self.view.get_context_data()

        self.assertEqual('-1', context['items']['a'])
        self.assertEqual('2', context['items']['b'])
        self.assertEqual('35', context['items']['c'])
        self.assertEqual(144, context['d'])
        self.assertEqual(-5.0, context['x1'])
        self.assertEqual(7.0, context['x2'])

        self.assertDictEqual({}, context['errors'])

    def test_a_and_b_and_c(self):
        """/quadratic/results/?a=1&b=12&c=38"""
        self.view.request = self.request.get('/quadratic/results/?a=1&b=12&c=38')

        context = self.view.get_context_data()

        self.assertEqual('1', context['items']['a'])
        self.assertEqual('12', context['items']['b'])
        self.assertEqual('38', context['items']['c'])
        self.assertEqual(-8, context['d'])
        self.assertEqual(None, context['x1'])
        self.assertEqual(None, context['x2'])

        self.assertDictEqual({'d': ERROR_D_NEGATIVE}, context['errors'])
        