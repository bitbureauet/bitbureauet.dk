from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.transaction import atomic


class Profile(AbstractUser):

    phone_number = models.IntegerField(
        null=True,
        blank=True
    )

    twitter_handle = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    on_call = models.BooleanField(
        default=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if self.on_call:
            # If we are saving with on_call set then we
            # have to set the profile currently on call to off call
            Profile.objects.filter(on_call=True).update(on_call=False)

        super().save(*args, **kwargs)

    @atomic
    def put_on_call(self):
        Profile.objects.filter(on_call=True).update(on_call=False)

        self.on_call = True
        self.save()
