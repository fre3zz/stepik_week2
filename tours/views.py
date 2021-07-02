from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render

# Create your views here.


def main_view(request):
    return render(request, template_name='tours/index.html')


def departure_view(request, departure: str):
    return render(request, template_name='tours/departure.html')


def tour_view(request, id: int):
    return render(request, template_name='tours/tour.html')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините! (Ошибка 404)')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините! (Ошибка 500)')
