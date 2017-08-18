from django.http import HttpResponse
from django.shortcuts import render

def results(request):
    return render(request, 'templates/results.html')
