FROM python:3.10

WORKDIR /myapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app
COPY ./proxies ./proxies
COPY ./targets ./targets

COPY setup.py .
RUN pip install -e .

ENV HOST "$HOST"
ENV PORT "$HOST"

COPY start_server.sh .
CMD ./start_server.sh
