#!/bin/bash

HEROKU_APP_NAME=your_app_name
HEROKU_API_KEY=your_heroku_api_key

# Mở lại Dyno
heroku ps:scale web=1 --app $HEROKU_APP_NAME --api-key=$HEROKU_API_KEY
