FROM python:2.7

MAINTAINER hyunju

RUN apt-get update

RUN apt-get -y upgrade

ADD /sqs_application /sqs_application

RUN pip install -r /sqs_application/requirements.txt
RUN pip install boto

EXPOSE 5000

RUN mkdir /data

WORKDIR /sqs_application

CMD python server.py
