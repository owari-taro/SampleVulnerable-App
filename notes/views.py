# INTENTIONALLY VULNERABLE code for testing security scanners. Do not deploy.
import subprocess

import requests
import yaml
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Note


def search(request):
    # SQL injection
    q = request.GET.get("q", "")
    with connection.cursor() as cur:
        cur.execute("SELECT id, title FROM notes_note WHERE title LIKE '%" + q + "%'")
        rows = cur.fetchall()
    return JsonResponse({"results": rows})


def hello(request):
    # Reflected XSS
    return HttpResponse("<h1>Hello " + request.GET.get("name", "") + "</h1>")


def read_file(request):
    # Path traversal
    with open("/srv/files/" + request.GET.get("name", "")) as f:
        return HttpResponse(f.read(), content_type="text/plain")


def ping(request):
    # Command injection
    out = subprocess.check_output("ping -c 1 " + request.GET.get("host", ""), shell=True)
    return HttpResponse(out)


def fetch(request):
    # SSRF
    r = requests.get(request.GET.get("url", ""), verify=False)
    return HttpResponse(r.text)


def load_yaml(request):
    # Unsafe deserialization
    data = yaml.load(request.body, Loader=yaml.Loader)
    return JsonResponse({"data": str(data)})


def go(request):
    # Open redirect
    return HttpResponseRedirect(request.GET.get("next", "/"))


def note_detail(request, note_id):
    # IDOR: no ownership/auth check
    note = Note.objects.get(pk=note_id)
    return JsonResponse({"title": note.title, "body": note.body})
