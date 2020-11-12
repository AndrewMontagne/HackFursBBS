FROM debian:stable-slim
RUN apt-get update
RUN (DEBIAN_FRONTEND=noninteractive apt-get -y install python3 python3-pip sudo)
COPY requirements.txt /root/
RUN pip3 install -r /root/requirements.txt 
RUN adduser --disabled-password --gecos "" bbs