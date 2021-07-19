from django.shortcuts import render
from .models import *

def index(request):

    ##
    ventas_realizadas_general_todo = Orden.objects.all()
    orden_sandwich_todo = OrdenSandwich.objects.all()
    ingrediente_sandwich_todo = IngredientesSandwich.objects.all()

    ventas_realizadas_general = []

    ## Recorrer todas las ordenes
    for i in ventas_realizadas_general_todo:
        sandwichesDeOrden = []

        ## Recorrer todos los sandwiches por orden
        for j in orden_sandwich_todo:
            ingredientesDeSandwich = []

            ## Si el sandwich x orden actual pertenece a la orden entonces
            if j.orden == i:
                ## Recorrer todos los ingredientes por sandwich
                for k in ingrediente_sandwich_todo:

                    if k.sandwich==j.sandwich:
                        ingredientesDeSandwich.append({'ingrediente':k.ingrediente.nombre,'precio':k.precio})

                sandwichesDeOrden.append({'elemento':j.sandwich, 'tamaño':j.sandwich.tamaño.nombre, 'precio':j.sandwich.precio, 'ingredientes':ingredientesDeSandwich})

        ventas_realizadas_general.append({'nombre':i.cliente,'fecha':i.fecha,'pedidos':sandwichesDeOrden,'total':i.total})

    print(ventas_realizadas_general)
 
    return render(request, 'app/index.html',{'ventas':ventas_realizadas_general})

