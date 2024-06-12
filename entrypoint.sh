#!/bin/sh


echo "Waiting for the database to start..."
sleep 10

# upgrade db
flask db upgrade

# start service
uwsgi --ini /app/uwsgi.ini
