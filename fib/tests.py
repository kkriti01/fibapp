from django.test import TestCase
from django.test import Client


class TestFib(TestCase):
    def test_fib_success_number(self):
        c = Client()
        response = c.get('/', {'number': 2})
        self.assertEqual(response.status_code, 200)

    def test_fib_success(self):
        c = Client()
        response = c.get('/', {'number': 'R'})
        self.assertEqual(response.status_code, 200)
