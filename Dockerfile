FROM mirekphd/python3.10-ubuntu20.04

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
