#!/bin/sh

python manage.py collectstatic --no-input --clear

exec "$@"  # run extra user commands