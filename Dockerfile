FROM python:3.13.4-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
