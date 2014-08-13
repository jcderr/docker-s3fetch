FROM ubuntu:14.04
MAINTAINER Jeremy Derr <jeremy@derr.me>

WORKDIR /opt/app
ADD . /opt/app
RUN apt-get update -qq; apt-get install -yq python-pip; pip install -r requirements.txt

CMD bash
