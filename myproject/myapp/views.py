from django.shortcuts import render
from .download_audio import baixar_video
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        url_digitada = request.POST.get("url_digitada")
        context = {"url_digitada": url_digitada} 

        if url_digitada: 
            audio_baixado = baixar_video(url_digitada)

            if audio_baixado:
                messages.success(request, "Download realisado com sucesso")
                return render(request, 'index.html', {"audio_baixado": audio_baixado})
            else:
                messages.error(request, "Não foi possível realizar o download")
                return render(request, 'index.html', context)

    return render(request, 'index.html')