#! /bin/sh
set -e

if [ "${FLASK_ENV}" = "gunicorn" ]; then
    exec gunicorn \
        -w 4 \
        -b 0.0.0.0:8000 \
        --worker-tmp-dir /dev/shm \
        "website:create_app()"
elif [ "${FLASK_ENV}" = "flask" ]; then
    export FLASK_APP=website
    export FLASK_ENV=development
    exec flask run --host 0.0.0.0 --port 8000
elif [ "$#" -gt 0 ]; then
    exec "$@"
else
    echo "Set FLASK_ENV to 'gunicorn' or 'flask', or pass a command to execute." >&2
    exit 1
fi
