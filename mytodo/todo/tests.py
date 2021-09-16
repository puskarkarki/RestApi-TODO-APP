from django.test import TestCase
from .models import Todo

# Create your tests here.

class TodoModel(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title ='first todo', body = 'this is todo body')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first todo')
        
    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expeccted_object_name = f'{todo.body}'
        self.assertEqual(expeccted_object_name, 'this is todo body')