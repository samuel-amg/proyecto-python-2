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
    path('api/sandwiches/<int:pk>/ingredients', ingredientesSandwichList.as_view()),
    path('api/sandwiches/<int:pk>/ingredients/<int:ingredient_pk>', ingredientesSandwichDetails.as_view()),
    path('api/orders', ordenList.as_view()),
    path('api/orders/<int:pk>', ordenDetails.as_view()),
    path('api/orders/<int:pk>/sandwiches', ordenSandwichList.as_view()),
    path('api/reports', ReportList.as_view())
]