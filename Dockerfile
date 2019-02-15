####################################################################
# Django container DockerFile for Resume App
####################################################################


FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -U pip
RUN pip install -r requirements.txt
