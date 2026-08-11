from pytubefix import YouTube

def baixar_video(url: str):
    diretorio = "/mediafiles"

    try:
        yt = YouTube(url)
        audio = yt.streams.get_audio_only()
        if not audio:
            return False

        audio.download(output_path=diretorio, 
                           filename="audiobaixado.mp3")
    except:
        return False

    
