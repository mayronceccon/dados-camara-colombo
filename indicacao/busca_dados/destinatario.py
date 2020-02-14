import re
from lib.util.string import sanitize, normalize
from indicacao.busca_dados.busca import Busca


class Destinatario(Busca):
    def recuperar(self, dados):
        regex = r"((?:Destinatário[:]?\s)(.*?)(?:\sAssunto:))"
        matches = re.search(regex, dados)
        if matches is not None:
            destinatario = sanitize(matches.group(2)).upper()
            return normalize(destinatario)
