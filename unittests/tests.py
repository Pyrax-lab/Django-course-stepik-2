from django.test import TestCase

from .models import Catalog




class FirstTest(TestCase):
    def test1(self):
        self.assertEqual(1, 1)
        self.assertTrue(False)

    def test1(self):
        self.assertEqual(1, 1)
        self.assertTrue(False)

    def test_up(self):
        self.assertEqual(1, 5)

class First2Test(TestCase):
    def test1(self):
        self.assertEqual(1, 1)
        self.assertTrue(False)

    def test1(self):
        self.assertEqual(1, 1)
        self.assertTrue(False)

    
    def setUp(self):
        self.client