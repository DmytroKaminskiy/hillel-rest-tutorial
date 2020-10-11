#!/usr/bin/env bash

git pull origin main &&
docker-compose up -d --build &&
docker exec backend python ./src/manage.py migrate &&
docker exec backend python ./src/manage.py collectstatic --noinput &&
docker-compose restart backend nginx
