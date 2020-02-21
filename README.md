# Cidadão na Câmara

Este projeto tem como objetivo agrupar e mostrar de uma forma clara, o que os vereadores estão propondo na Câmara de Vereadores de seus municípios.

- [Requisitos](#Requisitos)
- [Instalação](#Instalação)
- [Configuração](#Configuração)
- [Execução](#Execução)
- [Testes](#Testes)
- [Contribuição](#Contribuição)
- [Licença](#Licença)

---
## Requisitos
* Python3.7 ou superior
* docker
* docker-compose
* virtualenv

---
## Instalação

### Clonar Repositório
```bash
git clone git@github.com:mayronceccon/dados-camara-colombo.git
cd dados-camara-colombo
```

### Criar virtualenv
```python
python -m venv .venv
```

### Iniciar virtualenv
```bash
source .venv/bin/activate
```

### Instalar depedências
```bash
pip install -r requirements.txt
```

---
## Configuração

### Arquivo de Configuração
Criar o arquivo .env na raiz do projeto incluindo as constantes:

```
DEBUG=True
SECRET_KEY=

DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=

TIKA_PATH=/tmp
TIKA_LOG_PATH=/tmp
```

### Iniciar banco de dados
```bash
docker-compose up --build
```

### Migrar dados
```python
python manage.py migrate
```

---
## Execução
Dois passos são necessário para a execução do projeto:
- 1º - Iniciar o banco de dados
```bash
docker-compose up --build
```

- 2º - Iniciar o projeto com Django
```python
python manage.py runserver
```

---
## Testes

### Testes Unitários
```python
python manage.py test
```

### Relatório de Cobertura de Testes
```bash
coverage run manage.py test && coverage html
```

---
## Exportar e Importar dados
Exportar
```python
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > db.json
```
Importar
```python
python manage.py loaddata db.json
```

---
## Contribuição
Pull requests são bem vindos. Para grandes alterações, por favor abra um issue para discussão a respeito da alteração.

Por favor atualize os testes conforme suas modificações.

---
## Licença
- **[GPL](http://www.gnu.org/licenses/gpl-3.0.html)**
