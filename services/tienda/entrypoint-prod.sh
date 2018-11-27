#!/bin/sh
echo &quot;Waiting for postgres...&quot;
while ! nc -z tienda-db 5432; do
    sleep 0.1
done
echo &quot;PostgreSQL started&quot;

python manage.py run -h 0.0.0.0
#gunicorn -b 0.0.0.0:5000 manage:app