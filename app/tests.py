from django.test import TestCase
from app.models import MyModel


class TestMyModel(TestCase):

    def testRetrieve(self):
        self.assertRaises(MyModel.objects.get(pk=1))
