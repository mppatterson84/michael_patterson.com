from django.core.validators import MaxLengthValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from blog.managers import PostManager
from mysite.middleware import get_current_user


class Post(models.Model):
    title = models.CharField(max_length=110, validators=[MaxLengthValidator(100)])
    body = models.TextField()
    image = models.ImageField(upload_to='images/', max_length=250, blank=True)
    author = models.ForeignKey(
        'auth.User', default=get_current_user, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now, blank=False)
    updated_at = models.DateTimeField(default=timezone.now, blank=False)
    slug = models.SlugField(unique=True, max_length=110, blank=True, validators=[MaxLengthValidator(100)])
    published = models.BooleanField(default=False)
    categories = models.ManyToManyField('blog.PostCategory')
    
    objects = PostManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Post.objects.generate_unique_slug(self)
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
