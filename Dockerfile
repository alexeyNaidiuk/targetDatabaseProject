FROM python:3.10

WORKDIR /myapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./proxies ./proxies
COPY ./targets ./targets
COPY ./app ./app

COPY setup.py .
RUN pip install -e .

CMD ["sh", "-c", "uvicorn app.main:app --host=$APP_HOST --port=$APP_PORT"]