FROM python:3.8

WORKDIR /usr/src/candy-shop-api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./ ./

RUN pip install -U pip setuptools wheel && pip install -r requirements.txt

CMD ["/bin/bash"]
