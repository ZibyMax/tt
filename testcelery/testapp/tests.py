from django.test import TestCase

# Create your tests here.


class TestClass(TestCase):

    def test1(self):
        self.assertTrue(True)

    def test2(self):
        self.assertEqual(1, 2)

