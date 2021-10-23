FROM python:3.8-buster

WORKDIR /app

COPY . .
RUN python3.8 -m pip install "poetry"
RUN make build_and_install_local

CMD ["poetry", "run", "main.py"]
