from django.test import TestCase

# Create your tests here.
from myapp.models import content

class contentTest (TestCase):
    def setUp (self):
        content.objects.create(name="girl", description="girl", country="Russia", cost='0', count=1)
        content.objects.create(name="Boy", description="boy", country="NewZeland", cost='25', count=3)
    def test_how_much_pictures(self):
        summa=content.objects.get(id=1)
        self.assertEqual(summa.sum(),4)  

''' dsfdsf'''  
