import re
from indicacao.busca_dados.busca import Busca


class Numero(Busca):
    def recuperar(self, dados):
        regex = r"((?:N°[:]?[\s]?)([0-9]{1,})((?:\s{0,}Autor|Autora)))"
        matches = re.search(regex, dados.lstrip())
        if matches is not None:
            return int(matches.group(2))
