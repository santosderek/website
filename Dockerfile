FROM python:3.8-buster
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
COPY . .
ENV FLASK_ENV=gunicorn
ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]
