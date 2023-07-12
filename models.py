from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(primary_key=True, max_length=70)

    def __str__(self) -> str:
        return super().__str__()
    
class Mecanico(models.Model):
    nombre = models.CharField(primary_key=True, max_length=100)
    def __str__(self) -> str:
        return super().__str__()

class Trabajo(models.Model):
    idTrabajo=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100)
    mecanico=models.ForeignKey(Mecanico, on_delete=models.CASCADE, default='Nuevo Mecanico')
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    foto=models.ImageField(upload_to='fotos',null=True,default='fotos/noImg.jpg')
    descripcion=models.TextField(max_length=1000)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, default='Nueva Categoria')
    
    def __str__(self) -> str:
        return super().__str__()