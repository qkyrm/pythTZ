from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    poster = models.ImageField(upload_to = 'images/')
    trailer = models.URLField()

    def __str__(self):
        return self.title
