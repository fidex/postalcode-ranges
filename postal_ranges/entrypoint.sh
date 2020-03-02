#!/bin/sh
# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi
# ls -lrt /usr/src/app

python manage.py flush --no-input
python manage.py migrate
python manage.py createcachetable
# python manage.py findstatic -v 3 regex_builder.css
python manage.py collectstatic --no-input --clear
# python manage.py runserver 0.0.0.0:8000
exec "$@"
