FROM python:3.15.1-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
