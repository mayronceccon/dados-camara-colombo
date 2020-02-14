from django.test import TestCase
from indicacao.models import Indicacao
from pauta.models import Pauta
from vereador.models import Vereador
from indicacao.services import IndicacaoServices


class IndicacaoServiceTest(TestCase):
    pass
    # def test_recuperar_conteudo(self):
    #     arquivo = './indicacao/sessao_23_04_2019.pdf'

    #     service = IndicacaoServices()
    #     conteudo = service._recuperar_conteudo(arquivo)

    #     lista = service._recuperar_dados_lista(conteudo)

    #     # INDICACAO 1
    #     item = lista[0]

    #     numero = service._indicacao_numero(item)
    #     self.assertEqual(223, numero)

    #     autor = service._indicacao_autor(item)
    #     self.assertEqual('Renato Lunardon', autor)

    #     destinatario = service._indicacao_destinatario(item)
    #     self.assertEqual('SECRETARIA DE GOVERNO', destinatario)

    #     assunto_esperado = 'Venho solicitar a esta secretaria para que viabilize junto a Copel para a troca de alguns postes de luz da rede elétrica, bem como a substituição das luminárias existentes por novas com lâmpadas de LED de 200 watts, na Rua Presidente Faria, desde o início da Estrada da Ribeira até a Rodovia Régis Bittencourt, bairro Colônia Faria, neste município.'
    #     assunto = service._indicacao_assunto(item)
    #     self.assertEqual(assunto_esperado, assunto)

    #     # INDICACAO 2
    #     item = lista[10]

    #     numero = service._indicacao_numero(item)
    #     self.assertEqual(233, numero)

    #     autor = service._indicacao_autor(item)
    #     self.assertEqual('Vagner Brandão', autor)

    #     destinatario = service._indicacao_destinatario(item)
    #     self.assertEqual('SECRETARIA DE PLANEJAMENTO', destinatario)

    #     assunto_esperado = 'Pavimentação asfáltica da Rua da Arara, no bairro Arruda, em Colombo/PR.'
    #     assunto = service._indicacao_assunto(item)
    #     self.assertEqual(assunto_esperado, assunto)
