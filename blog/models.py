from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
import markdown


class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    title = models.CharField(max_length=255)

    slug = models.SlugField(editable=False)

    body = models.TextField()

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_body(self):
        return markdown.markdown(self.body)
