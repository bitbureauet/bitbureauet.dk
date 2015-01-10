from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django_extensions.db.fields import AutoSlugField

from core import mixins


class Post(mixins.MarkdownMixin, models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    title = models.CharField(max_length=255)

    slug = AutoSlugField(populate_from='title')

    body = models.TextField()

    published = models.BooleanField(default=False)

    edited_by = models.ManyToManyField('auth.User', editable=False)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
