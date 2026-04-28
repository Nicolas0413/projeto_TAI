FROM python:3.12-slim   

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY classes.py .
COPY arquivo.py .

EXPOSE 5000

CMD ["python", "app.py", "0.0.0.0:5000"]