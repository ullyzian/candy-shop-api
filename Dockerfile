FROM python:3.8

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "flask" ]

CMD [ "run" ]