from django.shortcuts import render
from .forms import QuadraticFrom
from .quad import Quadratic


def quadratic_results(request):
    if 'a' in request.GET or 'b' in request.GET or 'c' in request.GET:
        form = QuadraticFrom(request.GET)
    else:
        form = QuadraticFrom()

    context = {
        'form': form
    }

    if form.is_valid():
        context['result'] = Quadratic(**form.cleaned_data)

    return render(request, 'quadratic/results.html',  context)

