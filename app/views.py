from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def sample(request):
    return render(request, 'app/sample.html')

def sample2(request):
    return render(request, 'app/sample2.html')