FROM python:3.13.7-alpine

RUN adduser --disabled-password --gecos "" dailycatfacts_user
USER dailycatfacts_user

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app/main.py"]