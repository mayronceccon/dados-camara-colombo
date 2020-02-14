from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from bairro.views import BairroViewSet
from indicacao.views import IndicacaoViewSet
from pauta.views import PautaViewSet
from vereador.views import VereadorViewSet
from projeto_lei.views import ProjetoLeiViewSet
from executor.views import ExecutorViewSet
from pauta.views import PautaViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="API Cidadão na Câmara",
        contact=openapi.Contact(email="unofficialcamaracolombo@gmail.com"),
        url="https://api.cidadaonacamara.com.br",
        schemes="https"
        # license=openapi.License(name="BSD License"),
        # terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'bairros', BairroViewSet, basename='Bairro')
router.register(r'indicacoes', IndicacaoViewSet, basename='Indicacao')
router.register(r'pautas', PautaViewSet)
router.register(r'vereadores', VereadorViewSet)
router.register(r'projetos', ProjetoLeiViewSet)
router.register(r'executores', ExecutorViewSet)

urlpatterns = [
    url(
        r'^documentacao(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    url(
        r'^documentacao/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    path('api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
