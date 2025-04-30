import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pos.settings")
django.setup()

from admin1.models import FAQ

data = [
    ('Apakah ada file ppdb online?', '<a href="https://drive.google.com/file/d/1EXvbWGGMoZnuw5l7OH8NowreXhIQ_ckO/view" target="_blank">di sini</a>.'),

]

for question, answer in data:
    FAQ.objects.get_or_create(question=question, answer=answer)

print("Data FAQ berhasil diinput.")