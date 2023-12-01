FROM python:3.11-alpine

# Path: /app
WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

VOLUME ["/downloads"]

CMD ["python", "app.py"]
