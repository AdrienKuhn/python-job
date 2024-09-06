FROM python:3.12.5-alpine
RUN mkdir job
ADD . /job
ENTRYPOINT python job/run.py
