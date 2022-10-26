#!/bin/bash

/usr/local/bin/gunicorn --workers 1 --threads 1 --reload --bind "0.0.0.0:8000" temporadas.wsgi
