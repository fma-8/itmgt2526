from django.db import models
from django.contrib.auth.models import User

# Models here.
class Home(models.Model):
    name = models.CharField(max_length=50)
    id = models.IntegerField(primary_key=True)
    image_url = models.URLField(blank=True)
    description = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return f'{self.name}'