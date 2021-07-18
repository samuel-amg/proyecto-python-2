from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT

from django.db import models
from django.db.models.fields.related import ForeignKey

class Tamaño(models.Model):
    nombre = models.CharField(max_length=20, null=False)
    precio = models.FloatField(null=False)

    def __str__(self):
        return self.nombre

class Ingrediente(models.Model):
    codigo = models.CharField(max_length=2, null=False, unique=True)
    nombre = models.CharField(max_length=100, null=False)
    precio = models.FloatField(null=False)

    def __str__(self):
        return self.nombre

class Sandwich(models.Model):
    tamaño = models.ForeignKey(Tamaño, on_delete=RESTRICT)

    def listaDeIngredientes(self):
        all = IngredientesSandwich.objects.all()
        lista = all.filter(sandwich=self.id)
        string = ""
        for i in lista:
            string = string+str(i.ingrediente)+", "

        return string

    def __str__(self):
        return ("Sandwich #"+str(self.id)+" - "+str(self.tamaño)+" de "+ self.listaDeIngredientes()) ##??


class IngredientesSandwich(models.Model):
    sandwich = models.ForeignKey(Sandwich, on_delete=CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=CASCADE)

    def __str__(self):
        return (str(self.sandwich.id)+" "+str(self.ingrediente.nombre))


class Orden(models.Model):
    cliente = models.CharField(max_length=100, null=False, unique=False)
    total = models.FloatField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return ("Orden para "+self.cliente)

class OrdenSandwich(models.Model):  
    orden = models.ForeignKey(Orden, on_delete=CASCADE)
    sandwich = models.ForeignKey(Sandwich, on_delete=CASCADE)

    def __str__(self):
        return (str(self.orden) +" - "+ str(self.sandwich)) 

##################################################################################################