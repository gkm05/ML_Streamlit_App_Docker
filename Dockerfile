FROM python:3.10-alpine

RUN mkdir -p /home/app

COPY . /home/app

CMD ["app.py"]