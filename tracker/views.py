from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # or whatever your template is named
