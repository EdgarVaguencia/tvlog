from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import index, capitulos_list

urlpatterns = [
    path('capitulos/admin/', admin.site.urls),
    path('capitulos/', index),
    path('capitulos/list/', capitulos_list.as_view({'get': 'list'}), name='capitulo-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
