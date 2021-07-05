from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from blog.utils import get_unique_slug


class Post(models.Model):
    title = models.CharField(max_length=110)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', max_length=250, blank=True)
    author = models.ForeignKey(
        'auth.User', default='auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)
    slug = models.SlugField(blank=True)
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField('blog.PostCategory')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        get_unique_slug(self)
        self.updated_at = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})


class PostCategory(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=False, blank=True, default='slug')

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(PostCategory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Post Categories"

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug, })
