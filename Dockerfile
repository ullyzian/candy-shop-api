FROM python:3.8

WORKDIR /usr/src/api

COPY ./ ./

RUN pip install -U pip setuptools wheel && pip install -r requirements.txt

# Add docker-compose-wait tool
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait ./scripts/wait
RUN chmod +x ./scripts/wait

CMD ["./scripts/docker_script"]
