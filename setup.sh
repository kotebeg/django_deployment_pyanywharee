#!/bin/bash

set -e

echo "=== Django Project Setup ==="

# Create and activate virtual environment
echo "[1/4] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "[2/4] Installing dependencies..."
pip install django==5.0.3 pandas numpy plotly openpyxl

# Run migrations
echo "[3/4] Running migrations..."
python manage.py migrate

# Create superuser
echo "[4/4] Creating superuser..."
python manage.py createsuperuser

echo ""
echo "=== Setup complete ==="
echo "Run the server with:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/login/"
