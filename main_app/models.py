from django.db import models
from django.urls import reverse

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quote_id':self.id})