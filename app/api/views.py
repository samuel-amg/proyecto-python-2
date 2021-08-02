from django.http import Http404, response

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app.models import *
from app.api.serializers import *

# Tamaño del sandwich *************************************************************************
class TamañoList(APIView):
    def get(self, request, format=None):
        tamaños = Tamaño.objects.all()
        serializer = tamañoSerializer(tamaños, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = tamañoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class tamañoDetails(APIView):
    def get_object(self, pk):
        try:
            return Tamaño.objects.get(pk=pk)
        except Tamaño.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        tamaño = self.get_object(pk)
        serializer = tamañoSerializer(tamaño)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        tamaño = self.get_object(pk)
        serializer = tamañoSerializer(tamaño, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         tamaño = self.get_object(pk)
         tamaño.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


# Ingrediente del sandwich *************************************************************
class ingredienteList(APIView):
    def get(self, request, format=None):
        ingrediente = Ingrediente.objects.all()
        serializer = ingredienteSerializer(ingrediente, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ingredienteSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ingredienteDetails(APIView):
    def get_object(self, pk):
        try:
            return Ingrediente.objects.get(pk=pk)
        except Ingrediente.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        ingrediente = self.get_object(pk)
        serializer = ingredienteSerializer(ingrediente)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        ingrediente = self.get_object(pk)
        serializer = ingredienteSerializer(ingrediente, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         ingrediente = self.get_object(pk)
         ingrediente.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

# Sandwich ************************************************************************

class sandwichList(APIView):
    def get(self, request, format=None):
        sandwich = Sandwich.objects.all()
        serializer = sandwichSerializer(sandwich, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = sandwichSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class sandwichDetails(APIView):
    def get_object(self, pk):
        try:
            return Sandwich.objects.get(pk=pk)
        except Sandwich.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        sandwich = self.get_object(pk)
        serializer = sandwichSerializer(sandwich)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        sandwich = self.get_object(pk)
        serializer = sandwichSerializer(sandwich, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         sandwich = self.get_object(pk)
         sandwich.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)


# Ingredientes del sandwich **********************************************************************

class ingredientesSandwichList(APIView):
    def get(self, request, format=None):
        ingredientesSandwich = IngredientesSandwich.objects.all()
        serializer = ingredientesSandwichSerializer(ingredientesSandwich, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ingredientesSandwichSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ingredientesSandwichDetails(APIView):
    def get_object(self, pk):
        try:
            return IngredientesSandwich.objects.get(pk=pk)
        except Sandwich.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        ingredientesSandwich = self.get_object(pk)
        serializer = ingredientesSandwichSerializer(ingredientesSandwich)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        ingredientesSandwich = self.get_object(pk)
        serializer = ingredientesSandwichSerializer(ingredientesSandwich, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         ingredientesSandwich = self.get_object(pk)
         ingredientesSandwich.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

# Orden **************************************************************************

class ordenList(APIView):
    def get(self, request, format=None):
        orden = Orden.objects.all()
        serializer = ordenSerializer(orden, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        order_serializer = ordenSerializer(data={'cliente': request.data['cliente'],
                                                 'total': request.data['total'],
                                                 'fecha': request.data['fecha']})

        if order_serializer.is_valid():
            saved_order = order_serializer.save()

            for sandwich in request.data['sandwiches']:
                serializer = sandwichSerializer(data={'tamaño': sandwich['size']['id'], 'tamaño_precio': sandwich['size']['precio'], 'precio': sandwich['precio']})

                if serializer.is_valid():
                    try:
                        saved_sandwich = serializer.save()
                    except Exception:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    for extra in sandwich['extras']:
                        extra_serializer = ingredientesSandwichSerializer(data={'sandwich': saved_sandwich.id,
                                                                                'ingrediente': extra['id'],
                                                                                'precio': extra['precio']})

                        if extra_serializer.is_valid():
                            try:
                                extra_serializer.save()
                            except Exception:
                                return Response(extra_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return Response(extra_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

                    order_sandwich_serializer = ordenSandwichSerializer(data={'orden': saved_order.id,
                                                                              'sandwich': saved_sandwich.id})

                    if order_sandwich_serializer.is_valid():
                        try:
                            order_sandwich_serializer.save()
                        except Exception:
                            return Response(order_sandwich_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return Response(order_sandwich_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(order_serializer.data)
        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ordenDetails(APIView):
    def get_object(self, pk):
        try:
            return Orden.objects.get(pk=pk)
        except Orden.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        orden = self.get_object(pk)
        serializer = ordenSerializer(orden)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        orden = self.get_object(pk)
        serializer = ordenSerializer(orden, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         orden = self.get_object(pk)
         orden.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)

# Sandwich x Orden **************************************************************************

class ordenSandwichList(APIView):
    def get(self, request, format=None):
        ordenSandwich = OrdenSandwich.objects.all()
        serializer = ordenSandwichSerializer(ordenSandwich, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ordenSandwichSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ordenSandwichDetails(APIView):
    def get_object(self, pk):
        try:
            return OrdenSandwich.objects.get(pk=pk)
        except OrdenSandwich.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format = None):
        ordenSandwich = self.get_object(pk)
        serializer = ordenSandwichSerializer(ordenSandwich)
        return Response(serializer.data)

    def put(self, request, pk, format = None):
        ordenSandwich = self.get_object(pk)
        serializer = ordenSandwichSerializer(ordenSandwich, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
         ordenSandwich = self.get_object(pk)
         ordenSandwich.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)