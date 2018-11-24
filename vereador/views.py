from django.http import JsonResponse, HttpResponse
from .models import Vereador


def index(request):
    jsonresponse = []
    for vereador in Vereador.objects.all().order_by('-nome'):
        jsonresponse.append({
            "id": vereador.id,
            "nome": vereador.nome,
            "apelido": vereador.apelido,
            "data_nascimento": vereador.data_nascimento,
            "email": vereador.email,
            "telefone_gabinete": vereador.telefone_gabinete,
            "observacao": vereador.observacao,
            "foto": vereador.get_absolute_image_url()
        })

    return JsonResponse({"results": jsonresponse})
