#!/bin/sh

# Инициализираме базата данни
echo "Initializing database..."
python << END
from app import app, db
with app.app_context():
    db.create_all()
END

# Прилагаме миграциите
echo "Applying migrations..."
flask db upgrade

# Стартираме Flask
echo "Starting Flask server..."
exec flask run --host=0.0.0.0 