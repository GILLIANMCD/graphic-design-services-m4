from django.test import TestCase

# Create your tests here.

class PortfolioTests(TestCase):
    

    def test_str(self):
        test_name = portfolio(name='A portfolio')
        self.assertEqual(str(test_name), 'A Portfolio')
