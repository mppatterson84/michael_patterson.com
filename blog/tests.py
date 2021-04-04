from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.testuser1 = User.objects.create_user(
            username='testuser1',
            password='abc123'
        )

        # Create a blog post
        cls.test_post = Post.objects.create(
            title='Post Title',
            body='Body content...',
            author=cls.testuser1,
            published=True,
            slug=''
        )

        cls.test_post2 = Post.objects.create(
            title='Post Title',
            body='Body content...',
            author=cls.testuser1,
            published=False,
            slug=''
        )

        cls.test_post3 = Post.objects.create(
            title='Post Title',
            body='Body content...',
            author=cls.testuser1,
            published=False,
            slug='the-slug'
        )

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        expected_author = f'{post.author}'
        expected_slug = f'{post.slug}'
        expected_published = f'{post.published}'
        expected_category = f'{post.categories}'
        self.assertEqual(expected_title, 'Post Title')
        self.assertEqual(expected_body, 'Body content...')
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_slug, 'post-title')
        self.assertEqual(expected_published, 'True')

    def test_blog_content2(self):
        post = Post.objects.get(id=2)
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        expected_author = f'{post.author}'
        expected_slug = f'{post.slug}'
        expected_published = f'{post.published}'
        expected_category = f'{post.categories}'
        self.assertEqual(expected_title, 'Post Title')
        self.assertEqual(expected_body, 'Body content...')
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_slug, 'post-title-2')
        self.assertEqual(expected_published, 'False')

    def test_blog_content3(self):
        post = Post.objects.get(id=3)
        expected_title = f'{post.title}'
        expected_body = f'{post.body}'
        expected_author = f'{post.author}'
        expected_slug = f'{post.slug}'
        expected_published = f'{post.published}'
        expected_category = f'{post.categories}'
        self.assertEqual(expected_title, 'Post Title')
        self.assertEqual(expected_body, 'Body content...')
        self.assertEqual(expected_author, 'testuser1')
        self.assertEqual(expected_slug, 'the-slug')
        self.assertEqual(expected_published, 'False')
