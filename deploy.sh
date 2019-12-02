#!/bin/bash

git pull
/home/dados-colombo/dados-camara-colombo/venv/bin/pip3.7 install --upgrade pip
/home/dados-colombo/dados-camara-colombo/venv/bin/pip3.7 install -r requirements.txt
/home/dados-colombo/dados-camara-colombo/venv/bin/python3.7 manage.py collectstatic --no-input
/home/dados-colombo/dados-camara-colombo/venv/bin/python3.7 manage.py migrate --no-input
supervisorctl restart dados_colombo
