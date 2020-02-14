import re
from lib.util.string import normalize
from indicacao.busca_dados.busca import Busca


class Assunto(Busca):
    def recuperar(self, dados):
        regex = r"((?:Assunto[:]?\s)(.*))"
        matches = re.search(regex, dados)
        if matches is not None:
            assunto = matches.group(2).lstrip()
            return normalize(assunto)
