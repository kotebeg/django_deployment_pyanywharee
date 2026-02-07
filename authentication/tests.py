from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from authentication import views


class LoginPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login")
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_login_page_loads(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_login_valid_credentials(self):
        response = self.client.post(self.login_url, {
            "floatingInput_name": "testuser",
            "floatingPassword_name": "testpass123",
        })
        self.assertRedirects(response, reverse("apps_dashboard"))

    def test_login_invalid_credentials(self):
        response = self.client.post(self.login_url, {
            "floatingInput_name": "testuser",
            "floatingPassword_name": "wrongpass",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "invalid credentials")

    def test_login_url_resolves_to_view(self):
        view = resolve("/login/")
        self.assertEqual(view.func, views.login_view)


class RegisterPageTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("register")

    def test_register_page_loads(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_register_valid_data(self):
        response = self.client.post(self.register_url, {
            "username": "newuser",
            "password1": "SecurePass789!",
            "password2": "SecurePass789!",
        })
        self.assertRedirects(response, reverse("apps_dashboard"))
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_register_auto_logs_in(self):
        self.client.post(self.register_url, {
            "username": "newuser",
            "password1": "SecurePass789!",
            "password2": "SecurePass789!",
        })
        response = self.client.get(reverse("apps_dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_register_password_mismatch(self):
        response = self.client.post(self.register_url, {
            "username": "newuser",
            "password1": "SecurePass789!",
            "password2": "DifferentPass!",
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")
        self.assertFalse(User.objects.filter(username="newuser").exists())

    def test_register_duplicate_username(self):
        User.objects.create_user(username="existing", password="testpass123")
        response = self.client.post(self.register_url, {
            "username": "existing",
            "password1": "SecurePass789!",
            "password2": "SecurePass789!",
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/register.html")

    def test_register_url_resolves_to_view(self):
        view = resolve("/login/register")
        self.assertEqual(view.func, views.register_view)


class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.dashboard_url = reverse("apps_dashboard")
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_dashboard_requires_auth(self):
        response = self.client.get(self.dashboard_url)
        self.assertRedirects(response, reverse("login"))

    def test_dashboard_loads_for_authenticated_user(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/apps_dashboard.html")

    def test_dashboard_url_resolves_to_view(self):
        view = resolve("/login/apps_dashboard")
        self.assertEqual(view.func, views.apps_dashboard)


class LogoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )

    def test_logout_redirects_to_login(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("login"))

    def test_logout_clears_session(self):
        self.client.login(username="testuser", password="testpass123")
        self.client.get(reverse("logout"))
        response = self.client.get(reverse("apps_dashboard"))
        self.assertRedirects(response, reverse("login"))

    def test_logout_url_resolves_to_view(self):
        view = resolve("/login/logout")
        self.assertEqual(view.func, views.logout_view)


class PasswordResetTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123"
        )

    def test_password_reset_page_loads(self):
        response = self.client.get(reverse("password_reset"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/password_reset_form.html")

    def test_password_reset_sends_email(self):
        from django.core import mail
        response = self.client.post(reverse("password_reset"), {
            "email": "testuser@example.com"
        })
        self.assertRedirects(response, reverse("password_reset_done"))
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("testuser@example.com", mail.outbox[0].to)

    def test_password_reset_invalid_email_still_redirects(self):
        # Security: don't reveal if email exists
        response = self.client.post(reverse("password_reset"), {
            "email": "nonexistent@example.com"
        })
        self.assertRedirects(response, reverse("password_reset_done"))

    def test_password_reset_done_page_loads(self):
        response = self.client.get(reverse("password_reset_done"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/password_reset_done.html")

    def test_password_reset_complete_page_loads(self):
        response = self.client.get(reverse("password_reset_complete"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/password_reset_complete.html")

    def test_password_reset_url_resolves(self):
        view = resolve("/login/password_reset/")
        self.assertEqual(view.url_name, "password_reset")
