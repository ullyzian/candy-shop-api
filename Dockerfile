FROM python:3.8

WORKDIR /usr/src/api

COPY ./ ./

RUN pip install -U pip setuptools wheel && pip install -r requirements.txt

EXPOSE 5000


