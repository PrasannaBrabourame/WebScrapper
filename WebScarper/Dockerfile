# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:alpine
## Database Initailization
# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=webscarper Version=0.0.1


WORKDIR /app
ADD . /app


CMD ["scrapy" "runspider" "webscrapper.py"]