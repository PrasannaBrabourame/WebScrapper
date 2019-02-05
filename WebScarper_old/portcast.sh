#!/bin/sh
docker run --name postgres -e POSTGRES_PASSWORD=integra -d -p 5432:5432 postgres
pip install sqlalchemy pytest scrapy
cmd /k