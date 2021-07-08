import random

from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render

from data import tours, departures
# Create your views here.
# Для рендеринга меню departures передается каждому view, честно говоря, не понял как сделать элегантнее.


def main_view(request):
    # создаем случайный список из 6 туров
    random_6_tours = dict(random.sample(tours.items(), 6))
    return render(request, 'tours/index.html', {"random_6_tours": random_6_tours,  # 6 случайных туров
                                                "departures": departures  # места отправления для формирования меню
                                                })


def departure_view(request, departure: str):
    # создаем новый список туров, в которых tour.departure = departure
    # также передаем город отправления
    # создаем и передаем словарь cost - с минимальной и максимальной ценами туров
    # создаем и передаем словарь nights - с минимальной и максимальной продолжительностью туров
    # передаем departures для рендера меню

    try:
        # Проверка на правильность указания адреса
        departures[departure]
    except KeyError:
        raise Http404

    departure_tours = {tour_id: tour for (tour_id, tour) in tours.items() if tour["departure"] == departure}

    costs = {
        "maximum": max([tour.get("price") for tour in departure_tours.values()]),
        "minimum": min([tour.get("price") for tour in departure_tours.values()])
    }
    nights = {
        "maximum": max([tour.get("nights") for tour in departure_tours.values()]),
        "minimum": min([tour.get("nights") for tour in departure_tours.values()])
    }

    return render(request, 'tours/departure.html', {"dep_tours": departure_tours,  # туры из места отправления
                                                    "departure": departures.get(departure),  # место вылета
                                                    "costs": costs,  # словарь с мин и макс стоимостями
                                                    "nights": nights,  # словарь с мин и макс количеством ночей
                                                    "departures": departures  # места отправления для меню
                                                    })


def tour_view(request, tour_id: int):
    # Для отображения нужно количества звёзд создадим дополнительный range, позволящий отобразить
    # в template нужное количество звезд для тура, выбранного по id
    # Также передается город из которого вылет
    # Departures передается для рендера меню

    try:
        tour = tours[tour_id]
        star_range = range(int(tour["stars"]))
        departure = departures.get(tour["departure"])
    except KeyError:
        raise Http404

    return render(request, 'tours/tour.html', {"tour": tour,  # тур по tour_id
                                               "star_range": star_range,  # range для количества звезд
                                               "departure": departure,  # место вылета
                                               "departures": departures  # места отправления для формирования меню
                                               })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ой, что то сломалось... Простите извините! (Ошибка 404)')


def custom_handler500(request):
    return HttpResponseServerError('Ой, что то сломалось... Простите извините! (Ошибка 500)')
