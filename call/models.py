from django.db import models
from django.db.transaction import atomic


class PhoneNumber(models.Model):
    user = models.ForeignKey('auth.User')
    number = models.IntegerField()
    current = models.BooleanField(default=False)

    @atomic
    def activate(self):

        current = PhoneNumber.objects.get(current=True)
        current.current = False
        current.save()

        self.current = True
        self.save()
