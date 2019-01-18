from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name="Title")
    text = models.TextField(verbose_name="Content")
    DateOfPublished = models.DateTimeField(verbose_name="Published Date", auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
