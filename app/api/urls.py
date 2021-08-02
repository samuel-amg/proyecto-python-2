from django.urls import path
from app.api.views import *

urlpatterns = [
    # API paths
    path('api/sizes', TamañoList.as_view()),
    path('api/sizes/<int:pk>', tamañoDetails.as_view()),
    path('api/ingredients', ingredienteList.as_view()),
    path('api/ingredients/<int:pk>', ingredienteDetails.as_view()),
    path('api/sandwiches', sandwichList.as_view()),
    path('api/sandwiches/<int:pk>', sandwichDetails.as_view()),
    path('api/sandwich_ingredients', ingredientesSandwichList.as_view()),
    path('api/sandwich_ingredients/<int:pk>', ingredientesSandwichDetails.as_view()),
    path('api/orders', ordenList.as_view()),
    path('api/orders/<int:pk>', ordenDetails.as_view()),
    path('api/order_sandwich', ordenSandwichList.as_view()),
    path('api/order_sandwich/<int:pk>', ordenSandwichDetails.as_view())
]