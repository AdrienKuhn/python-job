FROM python:3.9-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
