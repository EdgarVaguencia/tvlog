# syntax=docker/dockerfile:1
From python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/capitulos
COPY . /home/capitulos/
COPY requeriments.txt /home/capitulos/
COPY scripts /opt/scripts
RUN pip install -r requeriments.txt
