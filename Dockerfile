FROM python:3.14.0-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
