from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email= 'test@email.com',
            password='secret',
        )
        self.post = Post.objects.create(
            title = "A",
            body = "B",
            author = self.user,
        )

    
    def test_string_representation(self):
        post = Post(title="A")
        self.assertEqual(str(post),post.title)