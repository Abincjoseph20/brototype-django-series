from django.db import models

class MovieInfo(models.Model):
    title=models.CharField(max_length=60)
    year=models.IntegerField(null=True)
    decription=models.TextField()