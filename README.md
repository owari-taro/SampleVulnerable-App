# SampleVulnerable-App

Deliberately vulnerable Django 3.2.0 app for evaluating security scanning agents. **Never deploy.**

## Run
```
uv sync   # Python 3.8-3.9 required (Pillow 8.1.0 has no 3.10 wheel)
uv run python manage.py makemigrations notes
uv run python manage.py migrate
uv run python manage.py runserver
```

The Django Ninja API is available at `/api/` (interactive docs at `/api/docs`);
its health endpoint is `/api/health`.

`pyproject.toml` is the uv project configuration; `requirements.txt` is retained
for pip-based tooling.

## Planted issues
- Outdated deps with known CVEs (Django 3.2.0, PyYAML 5.3.1, Pillow 8.1.0, requests 2.19.0)
- Settings: hardcoded `SECRET_KEY`, `DEBUG=True`, `ALLOWED_HOSTS=*`, no CSRF middleware, MD5 hasher, pickle sessions, non-HttpOnly cookie
- Views: SQL injection, reflected XSS, path traversal, command injection, SSRF, unsafe YAML load, open redirect, IDOR
