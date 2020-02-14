import re
from lib.util.string import normalize
from indicacao.busca_dados.busca import Busca


class Autor(Busca):
    def recuperar(self, dados):
        regex = r"((?:Autor[a]{0,}[:]?\s{0,})(.*?)(?:\s{0,}Destinatário))"
        matches = re.search(regex, dados)
        if matches is not None:
            autor = matches.group(2).split("(")[0].strip().lstrip()
            return normalize(autor)
