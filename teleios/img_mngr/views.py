from django.shortcuts import render

def home(request):
    return render(request, 'img_mngr/home.html', {})