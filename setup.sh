#!/bin/bash

set -e

echo "=== Django Project Setup ==="

# Step 1: Check and install Docker
echo "[1/7] Checking Docker..."
if command -v docker &> /dev/null; then
    echo "  Docker already installed: $(docker --version)"
else
    echo "  Installing Docker..."
    sudo apt update
    sudo apt install -y docker.io
    sudo usermod -aG docker $USER
    echo "  Docker installed. You may need to log out and back in for group changes."
fi

# Step 2: Check and install Docker Compose
echo "[2/7] Checking Docker Compose..."
if docker compose version &> /dev/null; then
    echo "  Docker Compose already installed: $(docker compose version --short)"
else
    echo "  Installing Docker Compose plugin..."
    sudo apt update
    sudo apt install -y docker-compose-plugin
    echo "  Docker Compose installed."
fi

# Step 3: Start PostgreSQL container
echo "[3/7] Starting PostgreSQL container..."
docker compose up -d
echo "  Waiting for PostgreSQL to be ready..."
sleep 3

# Step 4: Create and activate virtual environment
echo "[4/7] Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Step 5: Install dependencies
echo "[5/7] Installing dependencies..."
pip install django==5.0.3 pandas numpy plotly openpyxl python-dotenv psycopg2-binary

# Step 6: Generate .env with SECRET_KEY and DB config
echo "[6/7] Generating configuration..."
if [ ! -f .env ]; then
    SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
    cat > .env << EOF
SECRET_KEY=${SECRET_KEY}
DEBUG=True
DB_NAME=django_db
DB_USER=django_user
DB_PASSWORD=django_pass
DB_HOST=localhost
DB_PORT=5432
EOF
    echo "  Created .env with SECRET_KEY and database config"
else
    echo "  .env already exists, skipping..."
fi

# Step 7: Run migrations and create superuser
echo "[7/7] Running migrations..."
python manage.py migrate


# Step 8: Create demo user
echo "  Creating demo user (visitor/tester123)..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='visitor').exists():
    User.objects.create_user(username='visitor', password='tester123')
    print('  Demo user created.')
else:
    print('  Demo user already exists.')
"

echo ""
read -p "Create a superuser now? (y/n): " create_su
if [ "$create_su" = "y" ]; then
    python manage.py createsuperuser
fi

echo ""
echo "=== Setup complete ==="
echo "Run the server with:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit: http://127.0.0.1:8000/login/"
echo ""
echo "To stop PostgreSQL:  docker compose stop"
echo "To start PostgreSQL: docker compose up -d"