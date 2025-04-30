import requests
import json
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

def gemini_generate_content(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAigKPjOa_ahTeRtKHFHLV2qUIBNhEd1lI"

    headers = {
        "Content-Type": "application/json",
    }

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
# def generate_article_view(request):
#     article = ""
#     if request.method == 'POST':
#         topic = request.POST.get('topic')
#         prompt = f"Tulis artikel informatif tentang: {topic} dalam bahasa Indonesia"
#         article = gemini_generate_content(prompt)
#     return render(request, 'generate_article.html', {'article': article})


prompt = "Tulis artikel informatif tentang: Teknologi saat ini dalam bahasa Indonesia"
article = gemini_generate_content(prompt)
print(article)