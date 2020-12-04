FROM python:3.8.5

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update
# Install GnuText
RUN apt-get install -y gettext

RUN pip install --upgrade pip

WORKDIR /rocketdata

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .