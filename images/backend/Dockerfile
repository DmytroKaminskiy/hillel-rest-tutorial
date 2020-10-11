FROM python:3.9.0-slim

WORKDIR /home/ubuntu/projects/hillel_rest_tutorial
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENV PYTHONBREAKPOINT=ipdb.set_trace

COPY requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt
