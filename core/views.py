from django.http import JsonResponse
import requests
from datetime import datetime, timezone

def me(request):
    cat_fact = "Could not fetch cat fact at the moment 🐾"
    try:
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact", cat_fact)
    except requests.RequestException:
        pass

    data = {
        "status": "success",
        "user": {
            "email": "gloriaoluwafemi30@gmail.com",
            "name": "Gloria Oluwafemi",
            "stack": "Python/Django"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }
    return JsonResponse(data, status=200)
