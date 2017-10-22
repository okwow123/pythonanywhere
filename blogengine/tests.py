from django.test import TestCase
from django.utils import timezone
from blogengine.models import Post

# Create your tests here.

class PostTest(TestCase):
    def test_create_post(self):
        post = Post()
        post.title='title'
        post.text='text'
        post.pub_date=timezone.now()
        post.save

        all_posts=Post.objects.all()
	self.assertEquals(len(all_posts),1)
        only_post=all_posts[0]
        self.assertEquals(only_post,post)

        # Check attributes
        self.assertEquals(only_post.title, 'title')
        self.assertEquals(only_post.text, 'text')
        self.assertEquals(only_post.pub_date.day, post.pub_date.day)
        self.assertEquals(only_post.pub_date.month, post.pub_date.month)
        self.assertEquals(only_post.pub_date.year, post.pub_date.year)
        self.assertEquals(only_post.pub_date.hour, post.pub_date.hour)
        self.assertEquals(only_post.pub_date.minute, post.pub_date.minute)
        self.assertEquals(only_post.pub_date.second, post.pub_date.second)


