FROM python:3.8-buster

WORKDIR /app

ENV YOUR_ENV=${YOUR_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.0

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock /app/

COPY Makefile /app/
COPY solution/ /app/solution/
COPY main.py /app/

RUN make build_and_install_local

CMD ["poetry", "run", "python", "main.py"]
