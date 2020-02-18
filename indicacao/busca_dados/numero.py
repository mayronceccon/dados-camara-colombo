import re
from indicacao.busca_dados.busca import Busca


class Numero(Busca):
    def recuperar(self, dados):
        regex = r"((?:N[°|º][:]?[\s]?)([0-9]{1,})((?:\s{0,}Autor|\s{0,}Autora|\s{0,}Ano [0-9]{4})))"
        matches = re.search(regex, dados.lstrip())
        if matches is not None:
            return int(matches.group(2))
