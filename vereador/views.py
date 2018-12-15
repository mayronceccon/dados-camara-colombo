from django.http import JsonResponse, HttpResponse
from django.core.cache import cache
from .models import Vereador


def index(request):
    cache_key = 'vereador_list'
    # 23 horas
    cache_time = (60 * 60 * 23)
    data = cache.get(cache_key)

    if True:
        jsonresponse = []
        vereadores = Vereador.objects.all().order_by('nome')
        for vereador in vereadores:
            projetos = {
                'quantidade': vereador.projetos.count()
            }

            legislaturas = {
                'quantidade': len(vereador.legislaturas),
                'anos': vereador.legislaturas
            }

            jsonresponse.append({
                "id": vereador.id,
                "nome": vereador.nome,
                "apelido": vereador.apelido,
                "data_nascimento": vereador.data_nascimento,
                "email": vereador.email,
                "telefone_gabinete": vereador.telefone_gabinete,
                "observacao": vereador.observacao,
                "foto": vereador.get_absolute_image_url(),
                "projetos": projetos,
                "legislaturas": legislaturas
            })
        data = jsonresponse
        cache.set(cache_key, data, cache_time)

    return JsonResponse({"results": data})
