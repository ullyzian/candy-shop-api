FROM python:3.8

WORKDIR /usr/src/candy-shop-api

COPY ./ ./

RUN pip install -U pip setuptools wheel && pip install -r requirements.txt

CMD ["/bin/bash"]
