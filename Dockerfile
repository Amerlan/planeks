FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
COPY ./src /src
COPY requirements.txt /src/requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /src/requirements.txt
RUN apk del .tmp-build-deps
WORKDIR /src
