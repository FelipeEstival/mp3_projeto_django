from pytubefix import YouTube
from django.conf import settings

def baixar_video(url: str):
    diretorio = settings.MEDIA_ROOT

    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        if not audio:
            return False

        audio.download(output_path=diretorio, 
        filename="audiobaixado.m4a",
        skip_existing=False)

        return True
    except:
        return False

    
