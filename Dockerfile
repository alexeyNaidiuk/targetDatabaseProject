FROM python:3.10

WORKDIR /myapp

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app ./app
COPY setup.py .
RUN pip install -e .

COPY ./targets ./targets
COPY ./proxies ./proxies

CMD ["sh", "-c", "uvicorn app.main:app --host=$HOST --port=$PORT"]