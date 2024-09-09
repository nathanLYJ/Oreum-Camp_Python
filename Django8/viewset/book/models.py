from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    user = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title