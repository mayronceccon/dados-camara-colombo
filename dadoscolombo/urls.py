from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

from rest_framework import routers
from rest_framework import permissions

from bairro.views import BairroViewSet
from indicacao.views import IndicacaoViewSet
from pauta.views import PautaViewSet
from vereador.views import VereadorViewSet
from projeto_lei.views import ProjetoLeiViewSet
from executor.views import ExecutorViewSet

router = routers.DefaultRouter()
router.register(r'bairros', BairroViewSet, basename='Bairro')
router.register(r'indicacoes', IndicacaoViewSet)
router.register(r'pautas', PautaViewSet)
router.register(r'vereadores', VereadorViewSet)
router.register(r'projetos', ProjetoLeiViewSet)
router.register(r'executores', ExecutorViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('pautas/', include('pauta.urls')),
    path('projetos_lei/', include('projeto_lei.urls')),
    path('indicacoes/', include('indicacao.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
