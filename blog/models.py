from django.db import models
from django.core.urlresolvers import reverse


class Post(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)

    title = models.CharField(max_length=255)

    body = models.TextField()

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={'pk': self.pk})