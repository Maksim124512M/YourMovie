from django.db import models
import datetime

class Film(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    genre = models.CharField(max_length=50)
    actors = models.TextField(default='Actors')
    date = models.TextField(default='Date')
    contry = models.CharField(max_length=100, default='Country')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'


class Comment(models.Model):
    comment = models.CharField(max_length=500)

    def __str__(self):
        return self.comment
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'