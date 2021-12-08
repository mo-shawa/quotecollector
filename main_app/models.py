from django.db import models
from django.urls import reverse

FANTYPES =(
    ('C', 'Casual'),
    ('S', 'Stan'),
    ('R', 'Rabid')
)

# Create your models here.

class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=150)

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
