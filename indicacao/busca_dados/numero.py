import re
from indicacao.busca_dados.busca import Busca


class Numero(Busca):
    def recuperar(self, dados):
        inicio = "?:[Nn][°|º][:]?[\s]?|nº\s{0,}"
        numero = "?P<numero>[0-9]{1,}"

        padrao_fim_1 = "\s{0,}[Aa]utor"
        padrao_fim_2 = "\s{0,}[Aa]no\s{0,}[0-9]{4}\s{0,}[Aa]utor"
        padrao_fim_3 = "\/[0-9]{4}\s{1,}[Aa]utor"
        padrao_fim = "?:%s|%s|%s" % (padrao_fim_1, padrao_fim_2, padrao_fim_3)

        regex = "(%s)(%s)(%s)" % (inicio, numero, padrao_fim)
        regex = re.compile(regex)
        matches = re.search(regex, dados.lstrip())
        if matches is not None:
            return int(matches.group('numero'))
