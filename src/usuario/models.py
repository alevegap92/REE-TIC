from django.db import models

# Create your models here.
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=70)
    colegio = models.CharField(max_length=300)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=12)
	email = models.EmailField()
	domicilio = models.TextField()

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('alumno-detail', args=[str(self.id)])


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.nombre, self.apellido, self id)
