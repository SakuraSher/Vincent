from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="just a test")

    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')
        
class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists(self):
        resp = self.client.get('/')

    def test_view_url_byname(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(200,resp.status_code)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(200,resp.status_code)
        self.assertTemplateUsed(resp,'home.html')
