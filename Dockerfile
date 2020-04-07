FROM python:3.7

RUN pip install poetry

WORKDIR /tmp/api
COPY ./ ./
RUN poetry install

# Add docker-compose-wait tool
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait ./scripts/wait
RUN chmod +x ./scripts/wait
RUN chmod +x ./scripts/docker_script

CMD ["./scripts/docker_script"]
