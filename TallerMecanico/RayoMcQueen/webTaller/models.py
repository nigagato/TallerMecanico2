from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(primary_key=True,max_length=45)
    foto = models.ImageField(upload_to='foto',null=True)
    
    def __str__(self) -> str:
        return self.nombre
    
class Reparacion(models.Model):
    idReparacion= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    #precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    foto=models.ImageField(upload_to='foto',null=True,default='foto/default.avif')
    publicar=models.BooleanField(default=False)
    comentario=models.TextField(default='S/C')
    #usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nombre
    
    #en caso de añadirle precio:
    #def __str__(self) -> str:
    #    return self.nombre+" "+str(self.precio)
    