FROM python:3.8-buster
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN /usr/sbin/useradd -M uwsgi &&\
    /usr/sbin/usermod -L uwsgi &&\
    /bin/chown -R uwsgi:uwsgi .
EXPOSE 5000
COPY . .
CMD [ "uwsgi", "--ini", "uwsgi.ini", \
               "--uid", "uwsgi" ]
