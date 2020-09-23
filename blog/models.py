# apps/blog/models.py

from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    caption = models.CharField(max_length=128, blank=True)
    post = models.ForeignKey('BlogEntry', blank=True, on_delete=models.CASCADE, related_name='images')

    def hello(self):
        print('hello')

    def __str__(self):
        return "%s" % self.image.url


class BlogEntry(models.Model):
    TYPE_GROW = '#eee'
    TYPE_TIP = '#EA00A3'
    ENTRY_TYPES = (
        (TYPE_GROW, 'grow'),
        (TYPE_TIP, 'note')
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    time = models.DateTimeField()
    publish_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    tags = TaggableManager()

    class Meta:
        verbose_name_plural = 'Blog Entries'

    def get_absolute_url(self):
        return reverse("blog_post_detail", kwargs=dict(slug=self.slug))

    def __str__(self):
        return u"%s" % self.title

