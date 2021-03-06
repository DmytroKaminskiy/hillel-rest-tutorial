#!/usr/bin/env bash

docker exec -it backend flake8 ./src &&
docker exec -it backend pytest ./src/tests -s -x --cov=src --cov-report html --cov-fail-under=94 &&
docker exec backend pip check &&
docker exec backend python src/manage.py check &&
docker exec backend python src/manage.py makemigrations --check --dry-run &&
docker exec backend python src/manage.py collectstatic --noinput --dry-run &&
docker exec backend python src/manage.py validate_templates &&
docker-compose -f docker-compose.yml -f docker-compose-dev.yml config --quiet &&
docker exec nginx nginx -t
