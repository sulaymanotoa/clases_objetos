from django.db import models

# Create your models here
class Estudiantes( models.Model):
    cedula.models.charFile(primary_key=)(max_length=10)
    nombre = models.charField(max_length=30,blank=False)
    apeliido = models.textField(max_length=30, blank=False)
    dierecccion = models.CharField(max_length=30,blank=False)
    telefono = models.CharField(max_length=30,blank=False)

    def _str_(self):
        return self.nombre
    class Docente(models.Model)
    idDocente =. models.charFile(primary_key=)(max_length=10)
    nombre = models.charField(max_length=30,blank=False)
    apeliido = models.textField(max_length=30, blank=False)

    def _str_(self):
        class calificacion (models.Model):
            estudiante=models.ForeignKey(estudiantes,ondelete=Model)
         

        Estudiantes=models.ForeignKey(on_delete=)
    
     

