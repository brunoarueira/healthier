FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry'

WORKDIR /app

COPY ./backend/healthier .

RUN apk add --update --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    libffi-dev \
    musl-dev \
    libpq && \
    pip install poetry && \
    poetry install && \
    find /usr/local \
      \( -type d -a -name test -o -name tests \) \
      -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
      -exec rm -rf '{}' + && \
    apk del --no-cache .build-deps

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
