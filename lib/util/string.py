import re
import unicodedata


def normalize(conteudo):
    conteudo = conteudo.strip() \
        .rstrip('\r\n') \
        .replace("\n", "") \
        .replace("\r", "")
    return re.sub('[ ]{2,}', ' ', conteudo)


def sanitize(palavra):
    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavra = u"".join([c for c in nfkd if not unicodedata.combining(c)])

    # Usa expressão regular para retornar
    # a palavra apenas com números, letras e espaço
    return normalize(re.sub('[^a-zA-Z0-9 \\\]', ' ', palavra))
