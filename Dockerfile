ARG RUNTIME_IMAGE="python:3.10-alpine"

FROM ${RUNTIME_IMAGE} as install-requirements
    WORKDIR /usr/src/app
    COPY requirements.txt .
    RUN pip \
        install \
            --no-cache-dir \
            -r requirements.txt \
        ;

    COPY . .
    ENTRYPOINT [ "./docker-entrypoint.sh" ]
    EXPOSE 8000
    ENV FLASK_ENV=gunicorn
