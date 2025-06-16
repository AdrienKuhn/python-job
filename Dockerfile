FROM python:3.13.5-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
