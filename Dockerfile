FROM python:3.13.3-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
