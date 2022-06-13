from unicodedata import name
from django.db import models

# Create your models here.
class File(models.Model):
# create a model that store a file
    name = models.CharField(max_length=100)
    voice_record = models.FileField()

    def __str__(self):
        return self.name

