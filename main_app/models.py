from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

FANTYPES =(
    ('C', 'Casual'),
    ('S', 'Stan'),
    ('R', 'Rabid')
)

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cats_detail', kwargs={'pk': self.id})


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=150)
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.quote

    def get_absolute_url(self):
        return reverse('detail', kwargs={'quote_id':self.id})

class Fan(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField('Fan Acquisition Date')
    fantype = models.CharField(
        max_length=1,
        choices = FANTYPES,
        default = FANTYPES[0][0]
    )
    quote = models.ForeignKey(Quote,on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.get_fantype_display()} {self.name} on {self.date}"
    
    class Meta:
        ordering = ['-fantype']


