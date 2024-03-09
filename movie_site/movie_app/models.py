from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

class Comment(models.Model):
    comment = models.CharField(max_length=500)
