from unittest import TestCase
from blog.tests.post import Post
 
class PostTest(TestCase):
    def test_create_post(self):
        print("test_create_post")
        p = Post('Test', 'Test Content')
 
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)