#!/bin/bash

set -e

echo "=== Django Project Setup ==="

# Create and activate virtual environment
echo "[1/5] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "[2/5] Installing dependencies..."
pip install django==5.0.3 pandas numpy plotly openpyxl python-dotenv

# Generate unique SECRET_KEY
echo "[3/5] Generating unique SECRET_KEY..."
if [ ! -f .env ]; then
    SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
    echo "SECRET_KEY=${SECRET_KEY}" > .env
    echo "DEBUG=True" >> .env
    echo "  Created .env with unique SECRET_KEY"
else
    echo "  .env already exists, skipping..."
fi

# Run migrations
echo "[4/5] Running migrations..."
python manage.py migrate

# Create superuser
echo "[5/5] Creating superuser..."
python manage.py createsuperuser

echo ""
echo "=== Setup complete ==="
echo "Run the server with:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/login/"
