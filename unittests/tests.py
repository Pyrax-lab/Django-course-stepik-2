from django.test import TestCase, SimpleTestCase
from .models import Catalog 
# Create your tests here.

class CatalogModelTest(TestCase):
    """Тест модели каталога"""

    # def setUp(self):
    #     self.book = Catalog(title='First Django Book',
    #         ISBN='978-1-60309-3',
    #         author='Ilya Perminov',
    #         price='10',
    #         availability='True')
        
    #def test_create_book(self):

    def test_plus(self):
        response = 10 + 5
        return self.assertEqual(10, response)
    
    def test_plus2(self):
        response = 10 + 5
        return self.assertEqual(15, response)
    
    def test_plus3(self):
        response = 10 + 5 
        return self.assertEqual(15, response)