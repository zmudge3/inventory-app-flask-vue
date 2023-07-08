#!/usr/bin/env bash

docker build -t registry.heroku.com/frozen-thicket-91775/web .
docker push registry.heroku.com/frozen-thicket-91775/web
heroku container:release --app frozen-thicket-91775 web
heroku maintenance:off
