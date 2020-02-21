from django.test import TestCase
from .models import Editor,Article,tag
import datetime as dt

# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.ahmed= Editor(first_name = 'ahmed', last_name ='Mukhtar', email ='ahmed@moringaschool.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.ahmed,Editor))
    
    # Testing Save Method
    def test_save_method(self):
        self.ahmed.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
        
