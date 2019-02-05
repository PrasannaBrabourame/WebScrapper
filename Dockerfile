FROM python:alpine
WORKDIR /app
ADD . /app
ENTRYPOINT ["./execute.sh"]