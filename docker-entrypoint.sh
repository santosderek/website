#! /bin/sh
if [[ "$FLASK_ENV" == "gunicorn" ]]; then
    gunicorn -w 4 -b 0.0.0.0:8000 --worker-tmp-dir /dev/shm "website:create_app()"
elif [[ "$FLASK_ENV" == "flask" ]]; then
    export FLASK_APP=website
    export FLASK_ENV=development
    flask run --host 0.0.0.0 --port 8000
fi