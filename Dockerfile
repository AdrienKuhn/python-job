FROM python:3.14.6-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
