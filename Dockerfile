FROM python:3.13.0b1-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
