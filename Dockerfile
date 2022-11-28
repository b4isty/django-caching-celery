FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /app
