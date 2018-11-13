from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pautas/', include('pauta.urls')),
    path('admin/', admin.site.urls),
]
