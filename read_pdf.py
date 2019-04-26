#!/usr/bin/python3

from tika import parser
import re


def indicacao_numero(indicacao):
    regex = r"((?:N°[:]?\s)([0-9]{1,}?)(?:\sAutor|Autora))"
    matches = re.search(regex, indicacao)
    if matches is not None:
        return matches.group(2)


def indicacao_autor(indicacao):
    regex = r"((?:Autor[:]?\s|Autora[:]?\s)(.*?)(?:\sDestinatário))"
    matches = re.search(regex, indicacao)
    if matches is not None:
        return matches.group(2)


def indicacao_destinatario(indicacao):
    regex = r"((?:Destinatário[:]?\s)(.*?)(?:\sAssunto:))"
    matches = re.search(regex, indicacao)
    if matches is not None:
        return matches.group(2)


def indicacao_assunto(indicacao):
    regex = r"((?:Assunto[:]?\s)(.*))"
    matches = re.search(regex, indicacao)
    if matches is not None:
        return matches.group(2)

arquivo = 'http://www.camaracolombo.pr.gov.br/pauta/2018/sessao_27_11_2018.pdf'

raw = parser.from_file(arquivo)
content = raw['content']
content = content.strip().rstrip('\r\n').replace("\n", "").replace("\r", "").replace("  ", " ")
content = content.strip().rstrip('\r\n').replace("\n", "").replace("\r", "").replace("  ", " ")

# f = open('content.txt', 'w')
# f.write(content)
# f.close()

# print(content)
# exit()

regex = r"(?:cação\s)(.*?)(?:\sIndi|\sColombo, [0-9]{1,2} de|\sTribuna Livre)"
matches = re.findall(regex, content)
if matches is not None:
    for match in matches:
        numero = indicacao_numero(match)
        autor = indicacao_autor(match)
        destinatario = indicacao_destinatario(match)
        assunto = indicacao_assunto(match)
        text = "%s\n%s\n%s\n%s\n" % (numero, autor, destinatario, assunto)
        print(text)
