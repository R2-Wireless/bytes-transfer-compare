FROM python:3.11.4-slim as base

ENV PYTHONFAULTHANDLER 1
ENV PYTHONHASHSEED random
ENV PYTHONUNBUFFERED 1

WORKDIR /app

FROM base as builder
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -qq -y --no-install-recommends \
    zip \
    unzip \
    && \
    rm -rf /var/lib/apt/lists/* && apt-get clean
ENV PIP_DEFAULT_TIMEOUT 100
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PIP_NO_CACHE_DIR 1
ENV POETRY_VERSION 1.4.0

RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN . /venv/bin/activate && poetry install --no-dev --no-root

COPY . .
RUN . /venv/bin/activate && poetry build

FROM base as final

COPY --from=builder /venv /venv
COPY --from=builder /app/dist .

RUN . /venv/bin/activate && pip install *.whl
ENTRYPOINT [ "/bin/bash", "-c", ". /venv/bin/activate && eval \"$0 $*\"" ] 
CMD [ "start" ]
