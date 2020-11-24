FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN /usr/sbin/useradd -M uwsgi &&\
    /usr/sbin/usermod -L uwsgi &&\
    /bin/chown -R uwsgi:uwsgi .
EXPOSE 8080
CMD [ "uwsgi", "--ini", "website.ini", \
               "--uid", "uwsgi" ]
