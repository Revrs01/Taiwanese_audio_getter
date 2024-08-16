FROM python:3.10.14
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["waitress-serve", "--host=0.0.0.0", "--port=5647", "app:app"]