FROM python:3.7.4-buster
COPY ./src/* /src/
COPY ./requirements.txt /
RUN pip install -r requirements.txt