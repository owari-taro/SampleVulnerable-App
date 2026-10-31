# SampleVulnerable-App

Deliberately vulnerable Django 3.2.0 app for evaluating security scanning agents. **Never deploy.**

## Run
```
pip install -r requirements.txt   # Python 3.8-3.10 recommended
cd vulnapp && python manage.py makemigrations notes && python manage.py migrate && python manage.py runserver
```

## Planted issues
- Outdated deps with known CVEs (Django 3.2.0, PyYAML 5.3.1, Pillow 8.1.0, requests 2.19.0)
- Settings: hardcoded `SECRET_KEY`, `DEBUG=True`, `ALLOWED_HOSTS=*`, no CSRF middleware, MD5 hasher, pickle sessions, non-HttpOnly cookie
- Views: SQL injection, reflected XSS, path traversal, command injection, SSRF, unsafe YAML load, open redirect, IDOR
