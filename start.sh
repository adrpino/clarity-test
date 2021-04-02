#!/usr/bin/env bash

set -e

gunicorn -b 0.0.0.0:5000 -w 4 wsgi:app