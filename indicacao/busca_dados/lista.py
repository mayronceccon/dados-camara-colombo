import re
from indicacao.busca_dados.busca import Busca


class Lista(Busca):
    def recuperar(self, dados):
        regex = r"(?:cação\s)(.*?)(?:\sIndi|\sColombo, [0-9]{1,2} de|\sTribuna Livre)"
        return re.findall(regex, dados)
