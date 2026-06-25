ARG NODE_IMAGE="node:22-alpine"
ARG RUNTIME_IMAGE="python:3.10-alpine"

FROM ${NODE_IMAGE} as build-frontend
    WORKDIR /usr/src/app/frontend
    COPY frontend/package.json frontend/package-lock.json ./
    RUN npm ci
    COPY frontend/ ./
    RUN npm run build

FROM ${RUNTIME_IMAGE} as install-requirements
    WORKDIR /usr/src/app
    COPY requirements.txt .
    RUN python -m pip \
        install \
            --no-cache-dir \
            -r requirements.txt \
        ;

    COPY . .
    COPY --from=build-frontend /usr/src/app/website/static/spa ./website/static/spa
    RUN chmod +x ./docker-entrypoint.sh
    ENTRYPOINT [ "./docker-entrypoint.sh" ]
    EXPOSE 8000
    ENV FLASK_ENV=gunicorn
