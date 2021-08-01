from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    path('', index),
    path('', include('app.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
