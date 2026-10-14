FROM python:3.15.0-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
