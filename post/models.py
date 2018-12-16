from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name="Title")
    text = models.TextField(verbose_name="Content")
    DateOfPublished = models.DateTimeField(verbose_name="Published Date")

    def __str__(self):
        return self.title
