from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class UsersCategory(models.Model):
    teacher=models.CharField(max_length=255)
    student=models.CharField(max_length=250)
    bugalter=models.CharField(max_length=250)
    kassir=models.CharField(max_length=255)
    slug=models.CharField(max_length=250)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.teacher)
        super().save(*args, **kwargs)

    def __str__(self)-> str:
        return self.teacher