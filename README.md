# dados-camara-colombo

# Export/Import data
Export
```
python manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > db.json
```
Import
```
python manage.py loaddata db.json
```

# Coverage
```
coverage run manage.py test
```

```
coverage report
```

```
coverage html
```
