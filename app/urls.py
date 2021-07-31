from django.urls import path, include

from .views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path( '', index ),
    path('', include('app.api.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
