from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    views = models.IntegerField()
    is_published = models.BooleanField(default=True)
    date = models.DateField(("Date"), default=datetime.today())

    def __str__(self):
        return f'{self.name} - {self.author}'