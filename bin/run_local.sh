#!/bin/sh

docker compose down
# passing custom env-file
docker compose --env-file .env up --force-recreate --build