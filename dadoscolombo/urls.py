from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('pautas/', include('pauta.urls')),
    path('vereadores/', include('vereador.urls')),
    path('projetos_lei/', include('projeto_lei.urls')),
    path('indicacoes/', include('indicacao.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
