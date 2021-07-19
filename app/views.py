from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import *

def index(request):

    ## Listado de las ventas realizadas
    orden = Orden.objects.all()
    ordenSandwich = OrdenSandwich.objects.all()
    ingredientesSandwich = IngredientesSandwich.objects.all()
    sandwiches=Sandwich.objects.all()
    ingredientes=Ingrediente.objects.all()
    tamaños=Tamaño.objects.all()

    ventas_realizadas_general = []

    ## Recorrer todas las ordenes
    for i in orden:
        sandwichesDeOrden = []

        ## Recorrer todos los sandwiches por orden
        for j in ordenSandwich:
            ingredientesDeSandwich = []

            ## Si el sandwich x orden actual pertenece a la orden entonces
            if j.orden == i:
                ## Recorrer todos los ingredientes por sandwich
                for k in ingredientesSandwich:

                    if k.sandwich==j.sandwich:
                        ingredientesDeSandwich.append({'ingrediente':k.ingrediente.nombre,'precio':k.precio})

                sandwichesDeOrden.append({'elemento':j.sandwich, 'tamaño':j.sandwich.tamaño.nombre, 'precio':j.sandwich.precio, 'ingredientes':ingredientesDeSandwich})

        ventas_realizadas_general.append({'nombre':i.cliente,'fecha':i.fecha,'pedidos':sandwichesDeOrden,'total':i.total})

    ##########

    ## Listado de las ventas por día
    dias=[]
    for i in ventas_realizadas_general:
        if i['fecha'].date() not in dias:
            dias.append(i['fecha'].date())


    ## Listado de ventas por tamaño

    sandwich_por_tamaño=[]      ## Aqui se guarda un diccionario con cada tamaño y sus sandwiches correspondientes
    for i in tamaños:
        print(i)
        sandwich_de_este_tamaño=[]
        for j in sandwiches:
            if j.tamaño==i:
                orden_aux = orden.get(id=ordenSandwich.get(sandwich=j).orden.id)
                sandwich_aux = j
                sandwich_de_este_tamaño.append({'sandwich':sandwich_aux, 'orden':orden_aux})

        sandwich_por_tamaño.append({'tamaño':i.nombre,'sandwiches':sandwich_de_este_tamaño})

    #########################

    ## Listado de las ventas por ingredientes

    sandwich_por_ingrediente = []     ## Aqui se guarda un diccionario con cada ingrediente y sus correspondientes sandwiches
    for i in ingredientes:
        sandwich_con_este_ingrediente=[]
        for j in ingredientesSandwich:
            if j.ingrediente==i:
                orden_aux = orden.get(id=ordenSandwich.get(sandwich=j.sandwich).orden.id)
                sandwich_aux = sandwiches.get(id=ordenSandwich.get(sandwich=j.sandwich).sandwich.id)
                if {'sandwich':sandwich_aux,'orden':orden_aux} not in sandwich_con_este_ingrediente:
                    sandwich_con_este_ingrediente.append({'sandwich':sandwich_aux,'orden':orden_aux})
        sandwich_por_ingrediente.append({'ingrediente':i.nombre,'sandwiches':sandwich_con_este_ingrediente})
  
    #########################

    ## Listado de ventas por cliente

    clientes=[]
    for i in ventas_realizadas_general:
        if i['nombre'] not in clientes:
            clientes.append(i['nombre'])

    #########################

 
    return render(request, 'app/index.html',{'ventas':ventas_realizadas_general, 'dias':dias, 'sandwichPorTamaño':sandwich_por_tamaño, 'sandwichPorIngrediente':sandwich_por_ingrediente, 'clientes':clientes})

