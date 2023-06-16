FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install openpyxl
RUN pip install --upgrade pip
COPY . .
EXPOSE 8050
CMD ["python", "main.py"]
