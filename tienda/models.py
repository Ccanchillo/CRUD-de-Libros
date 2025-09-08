from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        db_table = 'book'
        managed = False
        ordering = ['title']

    def __str__(self):
        return f"{self.title} - {self.author}"
