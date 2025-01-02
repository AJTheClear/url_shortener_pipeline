FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Създаваме директорията instance
RUN mkdir -p instance

# Добавяме init-db скрипт
COPY init-db.sh .
RUN chmod +x init-db.sh

EXPOSE 5000

# Използваме init-db скрипта като entrypoint
ENTRYPOINT ["./init-db.sh"]
