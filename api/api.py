from ninja import NinjaAPI

api = NinjaAPI(title="Sample Vulnerable App API")


@api.get("/health")
def health(request):
    return {"status": "ok"}
