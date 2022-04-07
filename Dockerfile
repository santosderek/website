FROM python:3.10-alpine
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . .
ENV FLASK_ENV=gunicorn
ENTRYPOINT [ "./docker-entrypoint.sh" ]
