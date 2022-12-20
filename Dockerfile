FROM python:latest

ENV PYTHONUNBUFFERED 1
RUN mkdir /code

#LABEL Maintainer="thrifty.me"

WORKDIR /code

COPY test.py /code/

CMD [ "python", "./test.py"]