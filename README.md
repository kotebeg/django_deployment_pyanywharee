# Django Multi-App

A multi-app Django web application featuring authentication, signal visualization with interactive Plotly charts, and Excel file upload/download functionality.

**Live Demo:** [kotebeg.pythonanywhere.com/login/](https://kotebeg.pythonanywhere.com/login/)

> Demo credentials: `visitor` / `tester123`

## Features

- **Authentication** - Login and registration system with Django's built-in auth, session management, and a protected dashboard
- **User Registration** - Self-service account creation with email using custom `CustomUserCreationForm`, validation, and auto-login
- **Password Reset** - Secure password reset flow with email verification (console backend for demo, SMTP-ready for production)
- **Signal Visualization** - Generate random sinusoidal signals with Gaussian noise and render them as interactive Plotly line charts
- **Excel Upload/Download** - Upload Excel files containing signal data, visualize them, and download results as timestamped `.xlsx` files
- **Demo Credentials Modal** - One-click demo login with auto-fill credentials
- **Responsive UI** - Bootstrap 5.3 with light/dark/auto theme toggle
- **REST API** - Token-authenticated API endpoints for signal generation and data upload using Django REST Framework
- **Test Suite** - 48 unit tests covering authentication, registration, password reset, signal visualization, API endpoints, and URL routing
- **Dockerized Database** - PostgreSQL 15 running in Docker with persistent volumes
- **Secure Setup** - Unique SECRET_KEY generated automatically for each installation

## Tech Stack

| Layer          | Technology                          |
|----------------|-------------------------------------|
| Framework      | Django 5.0.3                        |
| Database       | PostgreSQL 15 (Docker)              |
| Frontend       | Bootstrap 5.3, Django Templates     |
| Visualization  | Plotly Express                      |
| API            | Django REST Framework (DRF)         |
| Data Processing| pandas, NumPy, openpyxl             |
| Testing        | Django TestCase (48 tests)          |
| Containerization| Docker, Docker Compose             |
| Deployment     | PythonAnywhere (WSGI)               |

## Project Structure

```
django-multi-app/
├── authentication/        # Login, registration, password reset & dashboard
│   └── forms.py           # CustomUserCreationForm with email field
├── signal_viz/            # Signal visualization & Excel processing
│   ├── views.py           # ProfileView (template-based)
│   ├── api_views.py       # REST API views (DRF)
│   ├── serializers.py     # DRF serializers
│   ├── api_urls.py        # API URL routing
│   ├── forms.py           # Excel upload form
│   └── signal_generator.py# Random signal generation & Plotly chart
├── config/           # Django project config (settings, urls, wsgi)
├── templates/             # Global templates (base.html, 404.html)
├── static/                # Global static files
├── docker-compose.yml     # PostgreSQL container config
├── manage.py
└── setup.sh               # Automated setup script (Docker + Django)
```

## Getting Started

### Prerequisites

- Python 3.10+
- Docker & Docker Compose

### Quick Start (using setup script)

The setup script automatically checks/installs Docker, starts PostgreSQL, creates a virtual environment, and runs migrations:

```bash
git clone <repository-url>
cd django-multi-app
chmod +x setup.sh
./setup.sh
source venv/bin/activate
python manage.py runserver
```

Visit [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd django-multi-app
   ```

2. **Start PostgreSQL with Docker**
   ```bash
   docker compose up -d
   ```

3. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install django==5.0.3 pandas numpy plotly openpyxl python-dotenv psycopg2-binary djangorestframework
   ```

5. **Generate `.env` configuration**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" > .env
   echo "DEBUG=True" >> .env
   echo "DB_NAME=django_db" >> .env
   echo "DB_USER=django_user" >> .env
   echo "DB_PASSWORD=django_pass" >> .env
   echo "DB_HOST=localhost" >> .env
   echo "DB_PORT=5432" >> .env
   ```

6. **Run migrations**
   ```bash
   python manage.py migrate
   ```

7. **Create a superuser** (or use the demo account)
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

### Docker Commands

```bash
docker compose up -d       # Start PostgreSQL
docker compose stop        # Stop PostgreSQL (data preserved)
docker compose down        # Stop and remove container (data preserved)
docker compose down -v     # Stop, remove container AND delete data
```

## URL Routes

| Path                     | Description                       |
|--------------------------|-----------------------------------|
| `/login/`                | Login page                        |
| `/login/register`        | User registration page            |
| `/login/logout`          | Logout (redirects to login)       |
| `/login/apps_dashboard`  | App dashboard (auth required)     |
| `/login/password_reset/` | Request password reset            |
| `/login/reset/<token>/`  | Set new password                  |
| `/signal_viz/`           | Signal upload & visualization     |
| `/signal_viz/get_excel`  | Download signal data as Excel     |
| `/api/v1/auth/token/`    | Obtain auth token (POST)          |
| `/api/v1/signals/generate/` | Generate random signal (GET)   |
| `/api/v1/signals/upload/`| Upload Excel, return JSON (POST)  |
| `/admin/`                | Django admin panel                |

## Testing

Run the full test suite (48 tests):

```bash
python manage.py test
```

Run tests by app:

```bash
python manage.py test authentication
python manage.py test signal_viz
```

Run a specific test class or method:

```bash
python manage.py test authentication.tests.DashboardTests
python manage.py test authentication.tests.LoginPageTests.test_login_valid_credentials
```

### Test Coverage

| App              | Test Class            | Tests | What's Covered                                              |
|------------------|-----------------------|-------|-------------------------------------------------------------|
| `authentication` | `LoginPageTests`      | 4     | Page load, valid/invalid login, URL resolution              |
| `authentication` | `RegisterPageTests`   | 6     | Page load, valid registration, auto-login, password mismatch, duplicate username, URL resolution |
| `authentication` | `DashboardTests`      | 3     | Auth required, authenticated access, URL resolution         |
| `authentication` | `LogoutTests`         | 3     | Redirect to login, session cleared, URL resolution          |
| `authentication` | `PasswordResetTests`  | 6     | Form load, email sent, invalid email handling, done/complete pages, URL resolution |
| `signal_viz`     | `SignalGeneratorTests`| 4     | DataFrame output, column names, row count, Plotly HTML      |
| `signal_viz`     | `SignalVizViewTests`  | 5     | Auth required (GET/POST), plot rendering, Excel upload, URL resolution |
| `signal_viz`     | `ExcelDownloadTests`  | 3     | Content type, file attachment, sheet data, URL resolution   |
| `signal_viz`     | `TokenAuthTests`      | 3     | Valid/invalid credentials, missing fields                   |
| `signal_viz`     | `GenerateSignalAPITests`| 6   | Auth required, JSON response, data structure, token auth, Excel download, URL resolution |
| `signal_viz`     | `UploadSignalAPITests`| 5     | Auth required, valid upload, missing file, data values, URL resolution |

## REST API

The project includes a REST API built with Django REST Framework. All API endpoints (except token authentication) require a valid token in the `Authorization` header.

### Authentication

Obtain a token by sending your credentials:

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/token/ \
  -d "username=visitor&password=tester123"
```

Response: `{"token": "your-token-here"}`

Use the token in subsequent requests:

```bash
curl -H "Authorization: Token your-token-here" \
  http://127.0.0.1:8000/api/v1/signals/generate/
```

### Endpoints

| Method | URL                          | Description                              |
|--------|------------------------------|------------------------------------------|
| POST   | `/api/v1/auth/token/`        | Obtain auth token (username + password)  |
| GET    | `/api/v1/signals/generate/`  | Generate random signal (JSON)            |
| GET    | `/api/v1/signals/generate/?output=xlsx` | Generate signal (Excel download) |
| POST   | `/api/v1/signals/upload/`    | Upload Excel file, return parsed JSON    |

### Example Response

```json
{
  "num_points": 700,
  "data": [
    {"time": 0, "random_signal": 0.1234},
    {"time": 1, "random_signal": 0.8765}
  ]
}
```

## Deployment (PythonAnywhere)

1. Upload the project to PythonAnywhere
2. Set up a virtual environment and install dependencies
3. Configure the WSGI file to point to `config.wsgi:application`
4. Set `ALLOWED_HOSTS` to your PythonAnywhere domain
5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
6. Reload the web app from the PythonAnywhere dashboard

## License

This project is for demonstration and learning purposes.
