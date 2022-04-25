FROM python:3.10

RUN mkdir /var/restaurant-finder

WORKDIR /var/restaurant-finder

COPY . /var/restaurant-finder/

ENTRYPOINT python /var/restaurant-finder/main.py