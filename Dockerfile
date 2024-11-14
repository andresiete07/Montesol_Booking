FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    sudo \
    iputils-ping \
    net-tools \
    wget \
    nano \
    python3-pip \
    xdg-utils 
    
COPY ./src/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

WORKDIR /home/src
EXPOSE 5000
CMD ["tail", "-f", "/dev/null"]
