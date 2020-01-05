FROM python:alpine
ENV PYTHONUNBUFFERED 1
ADD requirements.txt .
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev mariadb-connector-c-dev \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

WORKDIR /home

COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh / # backwards compat
RUN chmod +rx /usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["python", "/home/manage.py", "runserver", "0.0.0.0:8000"]