# syntax=docker/dockerfile:1

FROM --platform=linux/amd64 python:3.8-slim-buster as build

WORKDIR /whoami

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]