# syntax=docker/dockerfile:1
From python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /home/series
COPY . /home/series/
COPY requeriments.txt /home/series/
COPY scripts /opt/scripts
RUN pip install -r requeriments.txt
