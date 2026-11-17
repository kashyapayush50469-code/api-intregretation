import os, urllib.request, urllib.error

key = os.environ.get("GEMINI_API_KEY", "")
url = "https://generativelanguage.googleapis.com/v1beta/models"

req = urllib.request.Request(url, headers={"x-goog-api-key": key})

try:
    with urllib.request.urlopen(req, timeout=20) as r:
        print("Status:", r.status)
        print(r.read().decode()[:300])
except urllib.error.HTTPError as e:
    print("HTTP error:", e.code)
    print(e.read().decode()[:300])
except Exception as e:
    print("CONNECTION FAIL:", type(e).__name__, e)

    