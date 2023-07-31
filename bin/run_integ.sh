#!/bin/sh

docker compose -f ./docker-compose.integ.yml down
docker compose -f ./docker-compose.integ.yml up --force-recreate --build --remove-orphans --exit-code-from "myrepo_manager_integ"
