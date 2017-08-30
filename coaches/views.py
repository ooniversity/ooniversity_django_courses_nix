from django.views import generic
from coaches.models import Coach


class CoachDetailView(generic.DetailView):
    model = Coach
    template_name = 'coaches/detail.html'
