FROM python:3.12-alpine

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY ./src /app/src

CMD python3 /app/src/app.py