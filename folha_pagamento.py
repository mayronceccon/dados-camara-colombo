import requests
from zipfile import ZipFile
import xml.etree.ElementTree as ET
from datetime import datetime

exercicio = 2019
data_inicio = '20190301'
data_final = '20190331'

arquivoZip = './folha_pagamento_arquivos/%s_%s_%s.zip' % (exercicio, data_inicio, data_final)

url = 'http://intranet.camaracolombo.pr.gov.br/pronimtb/geraxml.asp?item=8&banco=DW_LC131_AP_0&exercicio=%s&dataInicial=%s&dataFinal=%s&unidadeGestora=-1&nmFornecedor=&TipoDespesa=0&TipoEsportacaoDados=2' % (exercicio, data_inicio, data_final)
requests.get(url)

r2 = requests.get('http://intranet.camaracolombo.pr.gov.br/pronimtb/dll/FolhaPagamento.zip')

open(arquivoZip, 'wb').write(r2.content)

with ZipFile(arquivoZip, 'r') as zipObj:
    with zipObj.open('FolhaPagamento.xml') as myfile:
        xmlstring = myfile.read()
        tree = ET.ElementTree(ET.fromstring(xmlstring))
        root = tree.getroot()

        for child in root:
            cargo = child.find('Cargo').text
            if cargo.upper() == 'VEREADOR':
                competencia = child.find('Competencia').text
                competencia = competencia.split('/')
                competencia = '%s-%s-%s' % (1, competencia[0], competencia[1])
                competencia = datetime.strptime(competencia, '%d-%m-%Y')

                salario_base = child.find('SalarioBase').text
                salario_base = salario_base.replace('R$ ', '')
                salario_base = salario_base.replace('.', '')
                salario_base = salario_base.replace(',', '.')
                salario_base = float(salario_base)

                nome_servidor = child.find('NomServidor').text
                print(competencia, nome_servidor, salario_base)
