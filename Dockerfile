FROM python:alpine
ENV LANG C.UTF-8
ENV TZ Asia/Tokyo
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev mariadb-connector-c-dev \
    && pip install --upgrade pip \
    && pip install poetry uwsgi \
    && poetry config virtualenvs.create false
WORKDIR /home

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
RUN chmod +rx /usr/local/bin/docker-entrypoint.sh

COPY uwsgi.ini /etc/

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["uwsgi", "--ini", "/etc/uwsgi.ini"]