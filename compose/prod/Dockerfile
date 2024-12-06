# pull official base image
FROM python:3.12.4-slim-bookworm

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG=0
ENV SECRET_KEY=foo
ENV DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1]

# Set environment variables for Poetry installation
ENV POETRY_VERSION=1.8.4 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="${POETRY_HOME}/bin:$PATH"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

# install system dependencies
RUN apt-get update \
  && apt-get -y install gcc postgresql \
  && apt-get clean


# add app
COPY . .

# add and run as non-root user
RUN adduser --disabled-password myuser
USER myuser

# run gunicorn
CMD gunicorn drf_project.wsgi:application --bind 0.0.0.0:$PORT
