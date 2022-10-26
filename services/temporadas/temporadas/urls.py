from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import index, temporadas_list

urlpatterns = [
    path('temporadas/admin/', admin.site.urls),
    path('temporadas/', index),
    path('temporadas/list/', temporadas_list.as_view({'get': 'list'}), name='temporada-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
