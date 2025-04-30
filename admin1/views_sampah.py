
# import openai
# from django.conf import settings
# from django.shortcuts import render, redirect
# from .forms import GeneratePromptForm, ArticleForm

# def gemini_generate_content(prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={settings.GEMINI_API_KEY}"

#     headers = {"Content-Type": "application/json"}
#     data = {
#         "contents": [
#             {
#                 "parts": [
#                     {"text": prompt}
#                 ]
#             }
#         ]
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(data))
#     if response.status_code == 200:
#         try:
#             result = response.json()
#             return result['candidates'][0]['content']['parts'][0]['text']
#         except (KeyError, IndexError):
#             return "Response format error."
#     else:
#         return f"API Error: {response.status_code} - {response.text}"
# openai.api_key = settings.OPENAI_API_KEY

# def chatbot_view(request):
#     response = None

#     if request.method == "POST":
#         user_question = request.POST.get("pertanyaan")
#         user_doc = nlp(user_question)

#         best_match = None
#         highest_score = 0.0

#         for faq in FAQ.objects.all():
#             faq_doc = nlp(faq.question)
#             score = user_doc.similarity(faq_doc)

#             if score > highest_score:
#                 highest_score = score
#                 best_match = faq

#         if highest_score > 0.75:  # Threshold bisa diatur
#             response = best_match.answer
#         else:
#             response = "Maaf, saya belum punya jawaban untuk pertanyaan itu."

#     return render(request, "frontend/chatbot.html", {"response": response})
# @csrf_exempt
# def chatbot_view(request):
#     if request.method == "POST":
#         user_question = request.POST.get("pertanyaan").lower()
#         if "jadwal" in user_question or "pelajaran" in user_question:
#             reply = "Jadwal pelajaran di sekolah kami dimulai pukul 07:30 hingga 14:00 setiap hari Senin sampai Jumat. Tersedia mata pelajaran seperti Matematika, Bahasa Indonesia, dan IPA."
#         elif "biaya" in user_question or "pendaftaran" in user_question:
#             reply = "Biaya pendaftaran sekolah kami adalah Rp 1.500.000 untuk tahun ajaran baru. Biaya ini termasuk seragam dan buku pelajaran."
#         elif "ekstrakurikuler" in user_question:
#             reply = "Kami memiliki berbagai kegiatan ekstrakurikuler seperti Basket, Pencak Silat, dan Pramuka. Kamu bisa mendaftar di awal tahun ajaran."
#         elif "fasilitas" in user_question:
#             reply = "Sekolah kami dilengkapi dengan laboratorium komputer, perpustakaan, dan ruang olahraga yang lengkap."
#         elif "kontak" in user_question or "alamat" in user_question:
#             reply = "Untuk informasi lebih lanjut, kamu bisa menghubungi kami di email: info@sekolahkami.sch.id atau datang langsung ke Jl. Pendidikan No. 123."
#         else:
#             reply = "Maaf, saya tidak bisa menjawab pertanyaan tersebut. Coba tanya tentang jadwal, biaya, fasilitas, atau kontak."

#         # headers = {
#         #     "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
#         #     "HTTP-Referer": "https://your-domain.com",  # ganti ke domain/webmu
#         #     "Content-Type": "application/json"
#         # }

#         # data = {
#         #     "model": "mistralai/mistral-7b-instruct",  # atau bisa juga "openai/gpt-3.5-turbo"
#         #     "messages": [
#         #         {"role": "user", "content": user_question}
#         #     ],
#         # }

#         # url = "https://openrouter.ai/api/v1/chat/completions"
#         # response = requests.post(url, headers=headers, json=data)

#         # if response.status_code == 200:
#         #     result = response.json()
#         #     reply = result["choices"][0]["message"]["content"]
#         # else:
#         #     reply = f"❌ Error: {response.json()}"

#         return JsonResponse({"response": reply})

#     return JsonResponse({"response": "Hanya menerima POST"})
# def generate_article(request):
#     if request.method == 'POST':
#         form = GeneratePromptForm(request.POST)
#         if form.is_valid():
#             topic = form.cleaned_data['topic']
#             response = openai.chat.completions.create(
#                 model="gpt-4o",
#                 messages=[
#                     {"role": "system", "content": "Kamu adalah penulis artikel untuk website sekolah."},
#                     {"role": "user", "content": f"Tulis artikel dengan tema: {topic}"}
#                 ],
#             )
#             content = response.choices[0].messages.content
#             # Redirect ke form editor dengan data awal
#             request.session['generated_title'] = topic
#             request.session['generated_content'] = content
#             return redirect('article_editor')
#     else:
#         form = GeneratePromptForm()
#     return render(request, 'artikel/generate_artikel.html', {'form': form})

# def article_editor(request):
#     initial = {
#         'title': request.session.get('generated_title', ''),
#         'content': request.session.get('generated_content', ''),
#     }
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('article_list')
#     else:
#         form = ArticleForm(initial=initial)
#     return render(request, 'edit_artikel.html', {'form': form})
# def generate_article(request):
#     if request.method == 'POST':
#         form = GeneratePromptForm(request.POST)
#         if form.is_valid():
#             topic = form.cleaned_data['topic']
#             prompt = f"Tuliskan artikel dengan tema '{topic}' yang menarik, rapi, dan sesuai untuk pembaca sekolah."

#             # Panggil ke Ollama lokal
#             response = requests.post(
#                 "http://localhost:11434/api/generate",
#                 json={"model": "mistral", "prompt": prompt, "stream": False}
#             )
#             result = response.json()
#             generated_content = result.get("response", "")

#             request.session['generated_title'] = topic
#             request.session['generated_content'] = generated_content
#             return redirect('article_editor')
#     else:
#         form = GeneratePromptForm()
#     return render(request, 'artikel/generate_artikel.html', {'form': form})

# def article_editor(request):
#     initial = {
#         'title': request.session.get('generated_title', ''),
#         'content': request.session.get('generated_content', ''),
#     }

#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('article_list')
#     else:
#         form = ArticleForm(initial=initial)
#     return render(request, 'artikel/edit_atikel.html', {'form': form})

# def generate_article(request):
#     if request.method == 'POST':
#         form = GeneratePromptForm(request.POST)
#         if form.is_valid():
#             topic = form.cleaned_data['topic']
#             prompt = f"Tuliskan artikel dengan tema '{topic}' yang menarik, rapi, dan sesuai untuk pembaca sekolah."

#             # Panggil ke Ollama lokal
#             response = requests.post(
#                 "http://localhost:11434/api/generate",
#                 json={"model": "mistral", "prompt": prompt, "stream": False}
#             )
#             result = response.json()
#             generated_content = result.get("response", "")

#             request.session['generated_title'] = topic
#             request.session['generated_content'] = generated_content
#             return redirect('article_editor')
#     else:
#         form = GeneratePromptForm()
#     return render(request, 'artikel/generate_artikel.html', {'form': form})

# def article_editor(request):
#     initial = {
#         'title': request.session.get('generated_title', ''),
#         'content': request.session.get('generated_content', ''),
#     }

#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('article_list')
#     else:
#         form = ArticleForm(initial=initial)
#     return render(request, 'artikel/edit_atikel.html', {'form': form})

