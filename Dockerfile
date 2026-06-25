ARG RUNTIME_IMAGE="python:3.10-alpine"

FROM ${RUNTIME_IMAGE} as backend
    WORKDIR /usr/src/app
    COPY requirements.txt .
    RUN python -m pip \
        install \
            --no-cache-dir \
            -r requirements.txt \
        ;

    COPY . .
    RUN chmod +x ./docker-entrypoint.sh
    ENTRYPOINT [ "./docker-entrypoint.sh" ]
    EXPOSE 8000
    ENV FLASK_ENV=gunicorn
