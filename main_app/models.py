from django.db import models

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.quote