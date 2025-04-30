import requests
from django.conf import settings
import json
def gemini_generate_content(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={settings.GEMINI_API_KEY}"

    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        try:
            result = response.json()
            return result['candidates'][0]['content']['parts'][0]['text']
        except (KeyError, IndexError):
            return "Response format error."
    else:
        return f"API Error: {response.status_code} - {response.text}"
def ai_generate_keywords(topic):
    prompt = (
        f"Buat 5-7 kata kunci SEO pendek (maksimal 3 kata per keyword), tanpa penjelasan, "
        f"dipisahkan dengan koma, untuk topik: {topic}. "
        f"Contoh format output: keyword1, keyword2, keyword3"
    )
    response = gemini_generate_content(prompt)
    keywords = [kw.strip() for kw in response.split(',') if kw.strip()]
    return keywords[:5]