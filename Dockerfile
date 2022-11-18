FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

ENV HOST "0.0.0.0"
ENV PORT "8181"

CMD ./start_server.sh
