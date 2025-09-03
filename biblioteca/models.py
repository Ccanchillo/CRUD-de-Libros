from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    author = models.CharField(max_length=100, verbose_name="Autor")
    published_date = models.DateField(verbose_name="Fecha de publicación")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libros"