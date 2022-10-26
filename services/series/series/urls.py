from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from .views import index, series_list

urlpatterns = [
    path('series/admin/', admin.site.urls),
    path('series/', index),
    path('series/list/', series_list.as_view({'get': 'list'}), name='serie-list'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
