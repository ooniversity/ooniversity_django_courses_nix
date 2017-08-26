from django.shortcuts import render, get_object_or_404
from .models import Coach


# Create your views here.
def detail(request, coach_id):
    coach_obj = get_object_or_404(Coach, pk=coach_id)

    return render(request, 'coaches/detail.html',
                  {'coach_obj': coach_obj})