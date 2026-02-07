# Django Deployment - PythonAnywhere

A multi-app Django web application deployed on PythonAnywhere, featuring signal visualization with interactive Plotly charts and Excel file upload/download functionality.

**Live Demo:** [kotebeg.pythonanywhere.com/login/](https://kotebeg.pythonanywhere.com/login/)

> Demo credentials: `visitor` / `tester123`

## Features

- **Authentication** - Login and registration system with Django's built-in auth, session management, and a protected dashboard
- **User Registration** - Self-service account creation using Django's `UserCreationForm` with validation and auto-login
- **Signal Visualization** - Generate random sinusoidal signals with Gaussian noise and render them as interactive Plotly line charts
- **Excel Upload/Download** - Upload Excel files containing signal data, visualize them, and download results as timestamped `.xlsx` files
- **Demo Credentials Modal** - One-click demo login with auto-fill credentials
- **Responsive UI** - Bootstrap 5.3 with light/dark/auto theme toggle
- **Test Suite** - 28 unit tests covering authentication, registration, signal visualization, and URL routing
- **Secure Setup** - Unique SECRET_KEY generated automatically for each installation

## Tech Stack

| Layer          | Technology                          |
|----------------|-------------------------------------|
| Framework      | Django 5.0.3                        |
| Database       | SQLite3                             |
| Frontend       | Bootstrap 5.3, Django Templates     |
| Visualization  | Plotly Express                      |
| Data Processing| pandas, NumPy, openpyxl             |
| Testing        | Django TestCase (28 tests)          |
| Deployment     | PythonAnywhere (WSGI)               |

## Project Structure

```
django_deployment_pyanywharee/
├── authentication/        # Login, registration & dashboard
├── signal_viz/            # Signal visualization & Excel processing
│   ├── views.py           # ProfileView (upload/plot), get_excel (download)
│   ├── forms.py           # Excel upload form
│   └── signal_generator.py# Random signal generation & Plotly chart
├── config/           # Django project config (settings, urls, wsgi)
├── templates/             # Global templates (base.html, 404.html)
├── static/                # Global static files
├── manage.py
├── setup.sh               # Automated setup script
└── db.sqlite3
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Quick Start (using setup script)

```bash
git clone <repository-url>
cd django_deployment_pyanywharee
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
   cd django_deployment_pyanywharee
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django==5.0.3 pandas numpy plotly openpyxl python-dotenv
   ```

4. **Generate unique SECRET_KEY**
   ```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(f'SECRET_KEY={get_random_secret_key()}')" > .env
   echo "DEBUG=True" >> .env
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (or use the demo account)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

## URL Routes

| Path                     | Description                       |
|--------------------------|-----------------------------------|
| `/login/`                | Login page                        |
| `/login/register`        | User registration page            |
| `/login/logout`          | Logout (redirects to login)       |
| `/login/apps_dashboard`  | App dashboard (auth required)     |
| `/signal_viz/`           | Signal upload & visualization     |
| `/signal_viz/get_excel`  | Download signal data as Excel     |
| `/admin/`                | Django admin panel                |

## Testing

Run the full test suite (28 tests):

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
| `signal_viz`     | `SignalGeneratorTests`| 4     | DataFrame output, column names, row count, Plotly HTML      |
| `signal_viz`     | `SignalVizViewTests`  | 5     | Auth required (GET/POST), plot rendering, Excel upload, URL resolution |
| `signal_viz`     | `ExcelDownloadTests`  | 3     | Content type, file attachment, sheet data, URL resolution   |

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
