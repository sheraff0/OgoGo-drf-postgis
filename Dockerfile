FROM python:3.11-slim-buster

# apt
RUN apt-get update --fix-missing -y && apt-get upgrade -y && apt-get install -y libmagic-dev gcc

# Geospatial libraries
RUN apt-get install -y binutils libproj-dev gdal-bin
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf /var/cache/apt

ADD requirements/dev.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt --disable-pip-version-check --no-cache-dir

COPY . /usr/src/project/
WORKDIR /usr/src/project/

