# Django Deployment - PythonAnywhere

A multi-app Django web application deployed on PythonAnywhere, featuring signal visualization with interactive Plotly charts, Excel file upload/download, and a monthly challenges module.

**Live Demo:** [kotebeg.pythonanywhere.com/login/](https://kotebeg.pythonanywhere.com/login/)

> Demo credentials: `visitor` / `tester123`

## Features

- **Authentication** - Login system with Django's built-in auth, session management, and a protected dashboard
- **Signal Visualization** - Generate random sinusoidal signals with Gaussian noise and render them as interactive Plotly line charts
- **Excel Upload/Download** - Upload Excel files containing signal data, visualize them, and download results as timestamped `.xlsx` files
- **Monthly Challenges** - Browse monthly programming challenges with month-based URL routing
- **Responsive UI** - Bootstrap 5.3 with light/dark theme toggle

## Tech Stack

| Layer          | Technology                          |
|----------------|-------------------------------------|
| Framework      | Django 5.0.3                        |
| Database       | SQLite3                             |
| Frontend       | Bootstrap 5.3, Django Templates     |
| Visualization  | Plotly Express                      |
| Data Processing| pandas, NumPy, openpyxl             |
| Deployment     | PythonAnywhere (WSGI)               |

## Project Structure

```
django_deployment_pyanywharee/
├── authentication/        # Authentication & dashboard
├── app26/                 # Monthly challenges
├── app27/                 # Redirect/error handling
├── file_upload/           # Signal upload, download & plotting
│   ├── views.py           # ProfileView (upload/plot), get_excel (download)
│   ├── forms.py           # Excel upload form
│   └── signal_generator.py# Random signal generation & Plotly chart
├── table_file_upload/     # Table file upload (stub)
├── labProjcets/           # Django project config (settings, urls, wsgi)
├── templates/             # Global templates (base.html, 404.html)
├── static/                # Global static files
├── manage.py
└── db.sqlite3
```

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

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
   pip install django==5.0.3 pandas numpy plotly openpyxl
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (or use the demo account)
   ```bash
   python manage.py createsuperuser
   ```

6. **Update settings for local development**

   In `labProjcets/settings.py`, set:
   ```python
   DEBUG = True
   ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

   Visit [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

## URL Routes

| Path                | Description                       |
|---------------------|-----------------------------------|
| `/login/`           | Login page                        |
| `/login/apps_dashboard` | App dashboard (auth required) |
| `/file_upload/`     | Signal upload & visualization     |
| `/file_upload/get_excel` | Download signal data as Excel |
| `/app26/`           | Monthly challenges index          |
| `/app26/<month>`    | Challenge for a specific month    |
| `/admin/`           | Django admin panel                |

## Deployment (PythonAnywhere)

1. Upload the project to PythonAnywhere
2. Set up a virtual environment and install dependencies
3. Configure the WSGI file to point to `labProjcets.wsgi:application`
4. Set `ALLOWED_HOSTS` to your PythonAnywhere domain
5. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
6. Reload the web app from the PythonAnywhere dashboard

## License

This project is for demonstration and learning purposes.
