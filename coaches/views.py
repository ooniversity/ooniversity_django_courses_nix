from django.shortcuts import render
from .models import Coach

# Create your views here.
def detail(request):
    courses_list = Coach.objects.all()

    return render(request, 'coaches/detail.html',
                  {'courses_list': courses_list})