import time
from google import genai
from google.genai import errors, types

client = genai.Client(
    http_options=types.HttpOptions(timeout=60000)  # 60 seconds (milliseconds mein)
)

MODELS = ["gemini-3.7-flash", "gemini-3.6-flash", "gemini-2.5-flash"]

def ask(prompt, retries=3):
    for model in MODELS:
        for attempt in range(retries):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                return response.text
            except (errors.ServerError, Exception) as e:
                wait = 2 ** attempt
                print(f"{model} fail: {type(e).__name__}. {wait}s baad retry...")
                time.sleep(wait)
        print(f"{model} se kaam nahi bana, agla model try kar raha hu...")
    raise RuntimeError("Abhi sab fail ho raha hai, internet ya server check karo")

print(ask("recurcion kay hota hai"))