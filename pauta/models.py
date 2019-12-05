from django.db import models


class Pauta(models.Model):
    descricao = models.CharField(max_length=100)
    link = models.URLField(max_length=255, unique=True)
    data_sessao = models.DateField()
    cadastro = models.DateTimeField(auto_now_add=True)
    indicacao_exportada = models.BooleanField(
        default=False,
        verbose_name=u'Indicacoes Exportadas'
    )

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "pauta"
        verbose_name_plural = "pautas"
