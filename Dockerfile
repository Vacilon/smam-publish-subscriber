FROM debian:bullseye-slim

RUN apt-get update
RUN apt-get install apache2 python3 python3-pip \
    libapache2-mod-wsgi-py3 python3-dev -y

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

# Additional bash configuration
SHELL ["/bin/bash", "-c"]
COPY ./config/bashrc /tmp
RUN cat /tmp/bashrc >> ~/.bashrc

# Application environment
WORKDIR /smam-app
COPY ./smam-app/requirements.txt ./
RUN pip3 install --no-cache-dir -r ./requirements.txt

EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]
