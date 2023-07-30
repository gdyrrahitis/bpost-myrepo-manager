#!/bin/sh

docker compose -f ./docker-compose.integ.yml down
docker compose -f ./docker-compose.integ.yml up --force-recreate --build
