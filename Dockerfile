FROM python:3.10-alpine as install-requirements
    WORKDIR /usr/src/app
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    COPY . .

FROM scratch as final
    ENTRYPOINT [ "./docker-entrypoint.sh" ]
    COPY --from=install-requirements / /
    EXPOSE 8000
    ENV FLASK_ENV=gunicorn
