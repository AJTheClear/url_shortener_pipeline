FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port for the Flask app
EXPOSE 5000

# Apply migrations and run the Flask app
CMD flask db upgrade && flask run --host=0.0.0.0
