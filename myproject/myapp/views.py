from django.shortcuts import render

# Create your views here.
def home(request):
    url_digitada = request.POST.get("url_digitada")

    return render(request, 'index.html')