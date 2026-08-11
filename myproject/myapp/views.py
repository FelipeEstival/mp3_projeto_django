from django.shortcuts import render
from download_audio import baixar_video
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        url_digitada = request.POST.get("url_digitada")
        context = {"url_digitada": url_digitada} 
            
        if baixar_video(url_digitada):
            messages.error(request, "Não foi possível realizar o download")
            return render(request, 'index.html', context)
        
        else:
            messages.success(request, "Download realisado com sucesso")
            return render(request, 'index.html', {"audio_baixado": "audio_baixado"})

    return render(request, 'index.html')