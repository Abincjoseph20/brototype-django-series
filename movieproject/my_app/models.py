from django.db import models

class MovieInfo(models.Model):
    title = models.CharField(max_length=60)
    year = models.IntegerField(null=True)
    decription =models.TextField()
    imgs = models.ImageField(upload_to='images/',null=True)

    def __str__(self):
        return self.title