# Pull base image
FROM python:3.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH "${PATH}:/root/.poetry/bin"

# Set work directory
WORKDIR /Disfactory

RUN apt-get update \
    && apt-get install -y nocache \
        binutils \
        curl

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python && \
    poetry config virtualenvs.create false

COPY pyproject.toml /Disfactory/
RUN poetry install

COPY . /Disfactory/

