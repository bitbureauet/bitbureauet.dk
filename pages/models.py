from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from core import mixins


class Page(mixins.MarkdownMixin, models.Model):

    title = models.CharField(max_length=50)

    slug = models.SlugField(editable=False)

    body = models.TextField()

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page:page-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)