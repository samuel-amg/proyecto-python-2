from enum import unique
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT

from django.db import models
from django.db.models.fields import FloatField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_delete, pre_delete, pre_save, post_save

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
    tamaño_precio = FloatField(default=0, null=False, blank=True)
    precio = models.FloatField(default=0)

    def listaDeIngredientes(self):
        all = IngredientesSandwich.objects.all()
        lista = all.filter(sandwich=self.id)
        string = ""
        for i in lista:
            string = string+str(i.ingrediente)+", "

        return string

    def calcularPrecio(self):
        all = IngredientesSandwich.objects.all()
        lista = all.filter(sandwich=self.id)
        total = self.tamaño_precio
        for i in lista:
            total = total+(i.precio)
        
        return total

    def save(self, force_insert=False, force_update=False):
        if not self.pk:
            self.tamaño_precio=self.tamaño.precio
        self.precio=self.calcularPrecio()

        super(Sandwich, self).save(force_insert, force_update)

    def __str__(self):
        return ("#"+str(self.id)+" - "+str(self.tamaño)+" de "+ self.listaDeIngredientes()) ##??


class IngredientesSandwich(models.Model):
    sandwich = models.ForeignKey(Sandwich, on_delete=CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=CASCADE)
    precio = models.FloatField(default=0, null=False, blank=True)

    def save(self, force_insert=False, force_update=False):
        if not self.pk:
            self.precio=self.ingrediente.precio
        super(IngredientesSandwich, self).save(force_insert, force_update)

    def __str__(self):
        return (str(self.sandwich.id)+" "+str(self.ingrediente.nombre))


class Orden(models.Model):
    cliente = models.CharField(max_length=100, null=False, unique=False)
    total = models.FloatField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True, blank=True)

    def calcularPrecio(self):
        all = OrdenSandwich.objects.all()
        lista = all.filter(orden=self.id)
        total = 0
        for i in lista:
            total = total+(i.sandwich.precio)
        
        return total

    def save(self, force_insert=False, force_update=False):
        self.total = self.calcularPrecio()
        super(Orden, self).save(force_insert, force_update)

    def __str__(self):
        return ("Orden para "+self.cliente)

class OrdenSandwich(models.Model):  
    orden = models.ForeignKey(Orden, on_delete=CASCADE)
    sandwich = models.ForeignKey(Sandwich, on_delete=CASCADE)

    def __str__(self):
        return (str(self.orden) +" - "+ str(self.sandwich)) 

###########

## Ocurre cuando hay un cambio de IngredientesSandwich, se vuelve a calcular el total del sandwich
def actualizarPrecioSandwich(sender, instance, **kwargs):

    # Actualizar precio sandwich
    t = Sandwich.objects.get(id=instance.sandwich.id)
    t.save()

    ## Actualizar precio orden cuando se actualice un sandwich
    try:
        orden = Orden.objects.get(id=OrdenSandwich.objects.get(sandwich=t).orden.id)
        orden.save()
    except:
        print("Fallo")   

post_save.connect(actualizarPrecioSandwich, sender=IngredientesSandwich)
post_delete.connect(actualizarPrecioSandwich, sender=IngredientesSandwich)

## Ocurre cuando hay un cambio de SandwichOrden
def actualizarPrecioOrden(sender, instance, **kwargs):
    t = Orden.objects.get(id=instance.orden.id)
    t.save()

post_save.connect(actualizarPrecioOrden, sender=OrdenSandwich)
post_delete.connect(actualizarPrecioOrden, sender=OrdenSandwich)

##################################################################################################