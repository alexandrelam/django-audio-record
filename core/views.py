from django.shortcuts import render
from .models import File

# Create your views here.

def home(request):
    if request.method == 'POST':
        print(request)
        print(request.POST)
        print(request.FILES)
        File.objects.create(voice_record=request.FILES['audio_data'] , name=request.POST['clip_name'])

    return render(request, "core/index.html")