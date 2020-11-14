FROM python:3.8-alpine

COPY . /app
WORKDIR /app

RUN apk add --virtual .build-deps build-base mariadb-connector-c-dev postgresql-dev unixodbc-dev && \
    pip install pipenv && \
    pipenv install --deploy --system && \
    chmod +x docker-entrypoint.sh && \
    apk --purge del .build-deps

EXPOSE 8000

ENTRYPOINT /app/docker-entrypoint.sh