FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r docker/requirements.txt

CMD ["python", "src/api/api.py"]

EXPOSE 5000
