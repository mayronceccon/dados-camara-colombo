#!/bin/bash

git pull
/home/dados-colombo/dados-camara-colombo/venv/bin/pip install -r requirements.txt
/home/dados-colombo/dados-camara-colombo/venv/bin/python manage.py collectstatic --no-input
/home/dados-colombo/dados-camara-colombo/venv/bin/python manage.py makemigrations --no-input
/home/dados-colombo/dados-camara-colombo/venv/bin/python manage.py migrate --no-input
supervisorctl restart dados_colombo