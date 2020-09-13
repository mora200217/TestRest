from django.db import models

# Create your models here.
class Book(models.Model):
    nombre = models.CharField(default='Nulo', max_length=250)
    año = models.DateField()
    autor = models.CharField(default='No hay autor',max_length=250)
    editorial = models.CharField(default='No hay editorial',max_length=250)

    class Meta:
        verbose_name = 'Mi Libro'
        verbose_name_plural = 'Mis Libros'
    
    def __str__(self):
        return "%i - %s escrito por %s " % (self.id,  self.nombre, self.autor)
        
    

